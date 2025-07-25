from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os
import asyncio

TOKEN = os.environ.get("TELEGRAM_TOKEN")

# 建立 Telegram Bot 應用
application = Application.builder().token(TOKEN).build()

# 定義 /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot 已啟動")

application.add_handler(CommandHandler("start", start))

# 建立 Flask App
app = Flask(__name__)

# Webhook 路由
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

# 啟動 Flask（for local debug，Render 不會跑這段）
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
