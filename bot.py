from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8429990932:AAE5criYIBQu4eJ6WapbQFpL7p4HhBsrGJ8"

WELCOME_MESSAGE = """🎉 Добро пожаловать в наш канал!

✅ Ваша заявка одобрена автоматически.

📋 Что у нас есть:
• Отборный и ежедневный контент
• Чат для общения и предложений

💡 Подписывайтесь на наши другие ресурсы:
👉 Канал 2: скоро будет!
👉 Группа: https://t.me/+gTDkVdfPWbkwZGNi

📢 Для связи: mode_dibil@mail.ru

Спасибо что с нами! 🚀
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
