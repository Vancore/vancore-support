import google.generativeai as genai
import json
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

SYSTEM_PROMPT = """
Ты — ассистент разработчика Даниила. Твоя задача — анализировать входящие сообщения.
ПРАВИЛА:
1. В конце ответа всегда добавляй строку через одну строчку: "Примечание: каждое сообщение обрабатывается независимо."
2. Никогда не используй символы: '<', '>', '&' (это ломает HTML-разметку).
3. Отвечай на том языке на которм было выслано сообщение
4. Категории: 
   - "ignore": спам, бред, простое приветствие или личные вопросы, не касающиеся разработки.
   - "thanks": благодарность.
   - "feedback": идеи/отзывы.
   - "important": баги/сотрудничество.
ЛОГИКА УВЕДОМЛЕНИЙ (notify_admin):
- Ставь "notify_admin": true ТОЛЬКО если сообщение содержит конкретную информацию (описание ошибки, шаги воспроизведения, суть идеи или четкое предложение).
- Если пользователь просто заявляет о намерении ("нашел баг", "есть идея", "хочу сотрудничать"), но НЕ пишет подробностей:
  1. Ставь "notify_admin": false.
  2. В "reply" вежливо поблагодари и попроси прислать детали сразу в следующем сообщении.
"""

model = genai.GenerativeModel(
    model_name='gemini-3.6-flash',
    system_instruction=SYSTEM_PROMPT,
    generation_config={
        "temperature": 0.1,
        "response_mime_type": "application/json"
    }
)

def analyze_message(user_text):
    prompt = f"""
    User message: "{user_text}"
    Return JSON: 
    {{"category": "string", "reply": "string", "notify_admin": boolean}}
    """
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        print(f"AI Error: {e}")
        return None



def generate_daily_summary(tickets):
    if not tickets:
        return "Сегодня сообщений не было."
    formatted_tickets = ""
    for user, text, cat in tickets:
        formatted_tickets += f"[{cat}] @{user}: {text}\n"
    prompt = f"""
    Ты — Chief of Staff разработчика Даниила. Перед тобой список сообщений за последние 24 часа:
    {formatted_tickets}

    Твоя задача — сделать краткий аналитический отчет:
    1. Общий настрой аудитории (Vibe Check).
    2. Список багов (если есть) — кратко.
    3. Лучшие идеи или предложения (если есть).
    4. Статистика: сколько всего сообщений, сколько благодарностей.

    Пиши профессионально, лаконично, в стиле минимализма. Используй эмодзи для акцентов.
    Никогда не используй символы: '<', '>', '&'.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Ошибка при создании сводки: {e}"
