import sqlite3
import threading

def connection_lock(func):
    def wrapper(self, *args, **kwargs):
        with self.lock:
            return func(self, *args, **kwargs)
    return wrapper

class Database:
    def __init__ (self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.lock = threading.Lock() 
        self.create_tables()

    #create
    @connection_lock
    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id BIGINT, username TEXT, message_text TEXT, category TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, is_answered BOOLEAN DEFAULT 0)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (user_id BIGINT PRIMARY KEY, username TEXT)''')
    #add
    @connection_lock
    def add_ticket(self, user_id, username, text, category="unknown"):
        with self.conn:
            self.conn.execute("INSERT INTO tickets (user_id, username, message_text, category) VALUES (?, ?, ?, ?)", (user_id, username, text, category))
    @connection_lock
    def add_user(self, user_id, username):
        with self.conn:
            self.conn.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))


    #time
    @connection_lock
    def count_recent_tickets(self, user_id, hours=24):
        with self.conn:
            cursor = self.conn.execute(f"SELECT COUNT(*) FROM tickets WHERE user_id = ? AND timestamp > datetime('now', '-{hours} hours')", (user_id,))
            return cursor.fetchone()[0]

    
    @connection_lock
    def mark_as_answered(self, ticket_id):
        with self.conn:
            self.conn.execute("UPDATE tickets SET is_answered = 1 WHERE user_id = ?", (ticket_id,))


    #Ai
    @connection_lock
    def get_todays_tickets(self):
        with self.conn:
            cursor = self.conn.execute("""SELECT username, message_text, category FROM tickets WHERE timestamp > datetime('now', '-24 hours')""")
            return cursor.fetchall()

    
db = Database("data.db")
            
