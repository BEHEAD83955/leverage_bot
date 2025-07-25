from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import os

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"

app = Flask(__name__)

# 初始化 telegram bot application（新版）
application = Application.builder().token(TOKEN).build()

# 處理 /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot 已啟動")

application.add_handler(CommandHandler("start", start))

# 設定 webhook 接收 telegram 的請求
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"

if __name__ == "__main__":
    app.run(port=5000)
