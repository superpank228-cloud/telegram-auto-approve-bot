# -*- coding: utf-8 -*-

import asyncio
import logging
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8429990932:AAE5criYIBQu4eJ6WapbQFpL7p4HhBsrGJ8"

USER_MESSAGE = 🎉 Добро пожаловать в наш канал!

✅ Ваша заявка одобрена автоматически.

📋 Что у нас есть:
• Отборный и ежедневный контент
• Чат для общения и предложений

💡 Подписывайтесь на наши другие ресурсы:
👉 Канал 2: скоро будет!
👉 Группа: https://t.me/+gTDkVdfPWbkwZGNi

📢 Для связи: mode_dibil@mail.ru

Спасибо что с нами! 🚀

logging.basicConfig(level=logging.INFO)

async def auto_approve_and_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    user = req.from_user
    chat = req.chat

    await context.bot.approve_chat_join_request(
        chat_id=chat.id,
        user_id=user.id
    )

    await context.bot.send_message(
        chat_id=user.id,
        text=f"👋 Привет, {user.full_name}!\n\n{USER_MESSAGE}"
    )

    print(f"✅ {user.full_name} принят")

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(auto_approve_and_message))
    print("🤖 Бот запущен и ждёт заявки...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
