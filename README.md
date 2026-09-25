<div align="center">

# 🛰️ Vancore Support

**An intelligent feedback terminal and AI triage gateway engineered for the Vancore digital ecosystem.**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/pyTelegramBotAPI-4.x-green?style=for-the-badge)](https://github.com/eternnoir/pyTelegramBotAPI)
[![AI Engine](https://img.shields.io/badge/Google_Gemini-Flash_AI-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![Database](https://img.shields.io/badge/Storage-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Daniil_Production-24A1DE?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DaniilProduction)

<br/>

**[English](README.md)** • **[Русский](README.ru.md)**

</div>

---

## 🧭 Overview & Philosophy

In a world overwhelmed by notifications, a creator's focused attention is the most scarce resource. Standard feedback bots either act as unmoderated mailboxes that drown the developer in noise, or rely on robotic auto-responders that frustrate users.

**Vancore Support** serves as a direct, intelligent interface between users and developer Daniil. 

Powered by **Google Gemini**, the system doesn't answer *for* the author — it acts as an architectural filter:
1. **Separates Signal from Noise:** Classifies incoming transmissions in real time, filtering out spam, off-topic inquiries, and low-effort messages.
2. **Context-Aware Triage:** Validates technical issues against Vancore's live product registry (DX Task, Metro Analysis, VPS Optimizer).
3. **Daily Executive Briefing:** Compiles raw feedback into an actionable 24-hour summary delivered directly to the developer's chat.

---

## 🏛 System Architecture

The project is built on a multi-tier pipeline separating interface routing, database concurrency, and AI processing:

```
 ┌────────────────────────────────────────────────────────┐
 │                     USER TRANSMISSION                  │
 └──────────────────────────┬─────────────────────────────┘
                            │
 ┌──────────────────────────▼─────────────────────────────┐
 │                  INTERFACE LAYER (bot.py)              │
 │  • Anti-Flood Guard (5 msgs / 12h)                     │
 │  • Native Admin Reply Router (#id<uid>)                │
 └─────────────┬────────────────────────────▲─────────────┘
               │                            │ Direct Reply
 ┌─────────────▼──────────────┐   ┌─────────┴─────────────┐
 │   DATABASE LAYER (data.py) │   │     ADMIN TERMINAL    │
 │  • Thread-safe Connection  │   │  • Actionable Alerts  │
 │  • Ticket State Tracking   │   │  • 19:00 Daily Digest │
 └─────────────┬──────────────┘   └─────────▲─────────────┘
               │                            │
 ┌─────────────▼────────────────────────────┴─────────────┐
 │                  AI INTELLIGENCE (ai_engine.py)        │
 │  • Gemini Flash Lite: Real-time Triage & JSON Extraction│
 │  • Gemini 3.6 Flash: 24h Chief-of-Staff Daily Summary  │
 │  • Dynamic Context Fetcher (Remote Product Registry)   │
 └────────────────────────────────────────────────────────┘
```

---

## ✨ Key Features

* **⚡ Real-Time AI Triage (`ai_engine.py`):** Every transmission is evaluated against strict technical domain boundaries. Messages are automatically categorized (`ignore`, `thanks`, `feedback`, `important`) with structured JSON extraction.
* **🌐 Multilingual Adaptation:** Automatic language detection. If the user writes in English, the gateway responds strictly in English; if in Russian, strictly in Russian.
* **📊 24-Hour Automated Digest:** A scheduled background thread synthesizes all daily tickets into a structured evening briefing at 19:00 (Vibe Check, Bug Registry, Actionable Ideas, Key Priority).
* **💬 Native Telegram Reply Bridging:** The developer replies directly to forwarded tickets using Telegram's native `Reply` feature. The bot matches the `#id` token and delivers the message back to the user seamlessly.
* **🛡 Anti-Flood Policy:** Strict quota of 5 messages per 12-hour window per user, ensuring high-signal communication.
* **🔄 Zero-Downtime Hot Reload:** Built-in `/reload` admin command allowing runtime updates of prompts and context without restarting the bot process.

---

## 📁 Repository Structure

```text
├── ai_engine.py         # Gemini AI pipeline: message analysis & 24h executive summary
├── bot.py               # Main bot runtime, scheduler loop & native reply router
├── config.example.py    # Environment configuration template
├── core.py              # System text templates & standard responses
├── data.py              # Thread-safe SQLite database manager
├── products_context.txt # Reference registry of Vancore ecosystem products
├── requirements.txt     # Project dependencies and packages
├── README.md            # Project documentation in English
└── README.ru.md         # Project documentation in Russian
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
* Python 3.10+
* A Telegram Bot Token from [@BotFather](https://t.me/BotFather)
* A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

### 2. Clone the Repository
```bash
git clone https://github.com/Vancore/vancore-support.git
cd vancore-support
```

### 3. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Credentials
Copy the configuration template:
```bash
cp config.example.py config.py
```
Open `config.py` and populate your secrets:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
ADMIN_ID = 123456789             # Your Telegram User ID (integer)
GOOGLE_API_KEY = "YOUR_GEMINI_KEY"
```

### 6. Run the Service
```bash
python bot.py
```
*The SQLite database (`data.db`) will initialize automatically on first boot.*

---

## ⌨️ Admin Commands

* **Reply to forwarded message:** Simply use Telegram's native Reply function on any forwarded insight containing `#id<uid>` to send an answer directly to the user.
* `/reload` — Hot-reloads `ai_engine.py` directly from source without restarting the bot.

---

### 🚀 Developments & Projects

All interactive essays, releases, and upcoming projects are published on Telegram:  
👉 **[@DaniilProduction](https://t.me/DaniilProduction)**
