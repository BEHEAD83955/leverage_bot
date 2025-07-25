from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# 從環境變數中讀取 Token
TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

# /start 指令的處理函數
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot 已啟動")

# 建立 Telegram Bot 應用
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Webhook 的接收路由
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "ok"

# Render 會訪問根目錄檢查服務是否活著
@app.route("/", methods=["GET"])
def home():
    return "Leverage Bot is running!"

if __name__ == "__main__":
    application.run_polling()