from telegram import Update
from telegram.ext import CallbackContext
from config import YC_API_KEY, YC_FOLDER_ID
import requests

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я бот-помощник по ПП. Выбери действие:",
        reply_markup=main_menu
    )

def handle_translate(update: Update, context: CallbackContext):
    update.message.reply_text("Введите текст для перевода:")

def translate_text(text: str, target_lang: str = "ru") -> str:
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    headers = {
        "Authorization": f"Api-Key {YC_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "folderId": YC_FOLDER_ID,
        "texts": [text],
        "targetLanguageCode": target_lang
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["translations"][0]["text"]

def ask_question(update: Update, context: CallbackContext):
    update.message.reply_text("Напишите вопрос специалисту:")

def send_question_to_support(question: str):
    # Здесь логика отправки вопроса (например, в Telegram чат поддержки)
    pass

def show_pp_tips(update: Update, context: CallbackContext):
    tips = [
        "✅ Пейте больше воды!",
        "✅ Ешьте больше овощей и фруктов.",
        "✅ Избегайте фастфуда."
    ]
    update.message.reply_text("\n".join(tips))