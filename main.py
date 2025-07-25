from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"

app = Flask(__name__)

# 建立 Telegram Application（新版寫法）
application = Application.builder().token(TOKEN).build()

# /start 指令處理
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Bot 已啟動成功！")

# 加入指令處理器
application.add_handler(CommandHandler("start", start))

# Webhook 處理函數
@app.route('/webhook', methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

# 本地測試可用（Render 上不會用到）
if __name__ == "__main__":
    app.run(port=5000)
