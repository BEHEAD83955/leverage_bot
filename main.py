import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 從環境變數中讀取 Telegram Token
TOKEN = os.getenv("TELEGRAM_TOKEN")

# 建立 Flask 應用程式
app = Flask(__name__)

# 初始化 Telegram Bot Application
application = Application.builder().token(TOKEN).build()

# /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot 已啟動 ✅")

# 加入指令處理器
application.add_handler(CommandHandler("start", start))

# webhook 路由
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"

# 執行 Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
