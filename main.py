import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

# 建立 Flask App
app = Flask(__name__)

# 建立 Telegram Bot 應用
application = ApplicationBuilder().token(TOKEN).build()

# 定義 /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot 已啟動，歡迎使用！")

# 加入指令處理器
application.add_handler(CommandHandler("start", start))

# Webhook 入口
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"

# 主程式（Render 自動執行）
if __name__ == "__main__":
    app.run(port=5000)
