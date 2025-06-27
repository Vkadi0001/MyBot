from telegram import ReplyKeyboardMarkup, KeyboardButton

# Главное меню (тема: ПП)
main_menu = ReplyKeyboardMarkup([
    ["🍏 Переводчик", "❓ Задать вопрос"],  
    ["💡 Советы по ПП", "🔙 Назад"]
], resize_keyboard=True)

# Кнопка "Назад"
back_button = KeyboardButton("🔙 Назад")