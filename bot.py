# -*- coding: utf-8 -*-

import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
)

BOT_TOKEN = "8429990932:AAE5criYIBQu4eJ6WapbQFpL7p4HhBsrGJ8"

USER_MESSAGE = """🎉 Добро пожаловать в наш канал!

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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user
    chat = join_request.chat

    try:
        # 1️⃣ принимаем заявку
        await context.bot.approve_chat_join_request(
            chat_id=chat.id,
            user_id=user.id
        )
        logging.info(f"Заявка принята: {user.id}")

        # 2️⃣ отправляем сообщение пользователю
        await context.bot.send_message(
            chat_id=user.id,
            text=f"👋 Привет, {user.full_name}!\n\n{USER_MESSAGE}",
            disable_web_page_preview=False
        )
        logging.info(f"Сообщение отправлено: {user.id}")

    except Exception as e:
        logging.error(f"Ошибка: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    app.run_polling()

if __name__ == "__main__":
    main()
