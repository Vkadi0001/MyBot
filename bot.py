from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start, handle_translate, ask_question, show_pp_tips
from keyboards import main_menu
from config import BOT_TOKEN

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("🍏 Переводчик"), handle_translate))
    dp.add_handler(MessageHandler(Filters.regex("❓ Задать вопрос"), ask_question))
    dp.add_handler(MessageHandler(Filters.regex("💡 Советы по ПП"), show_pp_tips))
    dp.add_handler(MessageHandler(Filters.regex("🔙 Назад"), start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()