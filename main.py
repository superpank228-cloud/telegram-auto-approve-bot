# -*- coding: utf-8 -*-

import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
)

# 🔐 Берём токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден. Добавь его в переменные окружения.")

USER_MESSAGE = """🎉 Добро пожаловать в наш канал!

✅ Ваша заявка одобрена автоматически.

📋 Что у нас есть:
• Отборный и ежедневный контент
• Чат для общения и предложений

💡 Подписывайтесь на наши другие ресурсы:
👉 Канал 2: скоро будет!
👉 Группа: https://t.me/+gTDkVdfPWbkwZGNi

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
        # 1️⃣ Принимаем заявку
        await context.bot.approve_chat_join_request(
            chat_id=chat.id,
            user_id=user.id
        )
        logging.info(f"Заявка принята: {user.id}")

        # 2️⃣ Пишем пользователю
        await context.bot.send_message(
            chat_id=user.id,
            text=f"👋 Привет, {user.full_name}!\n\n{USER_MESSAGE}",
            disable_web_page_preview=False
        )
        logging.info(f"Сообщение отправлено: {user.id}")

    except Exception as e:
