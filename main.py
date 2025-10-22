from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from config import telegram_bot_api
from read_json import answer


TOKEN = telegram_bot_api


# --- /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это Axon — твой проводник в мир науки и новых идей.\n"
        "Напиши мне тему (например: 'биотехнологии' или 'AI в медицине'), и я покажу исследования."
    )


# --- /help ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я понимаю команды /start и /help, а также любые текстовые запросы.\n"
        "Попробуй написать, например: 'новости биоинформатики' или 'исследования по экологии'."
    )


# --- Обработка текстовых сообщений ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = answer(user_message)
    await update.message.reply_text(response)


def main():
    app = Application.builder().token(TOKEN).build()

    # --- Команды ---
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # --- Сообщения ---
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот Axon запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
