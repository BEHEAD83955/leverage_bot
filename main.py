import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 使用環境變數方式獲取 TOKEN
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

# 定義 /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot 已啟動成功！")

# 建立 Telegram Application 並加入指令處理器
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# 處理 Telegram webhook 資料
@app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

# 本地測試（Render 不會用這段）
if __name__ == "__main__":
    app.run()
