import telebot
from config import TOKEN, ADMIN_ID
from data import db
import core

bot = telebot.TeleBot(TOKEN)

def is_flooding(uid):
    limit = 3
    count = db.count_recent_tickets(uid)
    if count >= limit:
        text = (
            "<b>Daily Limit Reached</b>\n\n"
            "You've sent 3 messages today. I limit this to ensure I can "
            "provide quality responses to everyone.\n\n"
            "Try again in 24 hours. See you then."
        )
        bot.send_message(uid, text, parse_mode="HTML")
        return True
    return False


@bot.message_handler(commands=['start'])
def start_handler(message):
    uid = message.chat.id
    if is_flooding(uid): return
    db.add_user(uid, message.from_user.username)
    text = core.welcome(uid)
    bot.send_message(uid, text, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.reply_to_message is not None)
def admin_reply_handler(message):
    if message.from_user.id != int(ADMIN_ID):
        return
    try:
        original_text = message.reply_to_message.text
        if "#id" not in original_text:
            return
        user_id = original_text.split("#id")[-1].strip()
        answer_text = message.text
        formatted_answer = (
            f"Response from Vancore:\n\n"
            f"{answer_text}"
        )
        bot.send_message(user_id, formatted_answer)
        db.mark_as_answered(user_id)
        bot.send_message(ADMIN_ID, "✅ Response sent.")
    except Exception as e:
        bot.send_message(ADMIN_ID, f"❌ Error sending response: {e}")

@bot.message_handler(func=lambda message: True)
def all_handler(message):
    if message.chat.type != 'private':
        return
    uid = message.chat.id
    if not message.text: 
        return
    if is_flooding(uid): 
        return
    username = message.from_user.username
    db.add_user(uid, username)
    db.add_ticket(uid, username, message.text)
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    full_name = f"{first_name} {last_name}".strip()
    admin_msg = (
        f"📩 New Insight\n"
        f"From: {full_name} @{username}\n"
        f"ID: {uid}\n"
        "-------------------\n\n"
        f"{message.text}\n\n"
        "-------------------\n"
        f"#id{uid}"
    )
    bot.send_message(ADMIN_ID, admin_msg)
    text = core.ticket_received(uid)
    bot.send_message(uid, text, parse_mode="HTML")


bot.infinity_polling()