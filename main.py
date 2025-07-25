from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"
WEBHOOK_URL = "https://leverage-bot-k0l8.onrender.com/webhook"  # 替換成你的 render 網址

app = Flask(__name__)

bot_app = ApplicationBuilder().token(TOKEN).build()

# 指令處理器
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 倉位機器人已啟動！")

bot_app.add_handler(CommandHandler("start", start))

# Flask 接收 Telegram Webhook
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return "ok", 200

# 設定 Webhook（只需執行一次）
@app.before_first_request
async def setup_webhook():
    await bot_app.bot.set_webhook(WEBHOOK_URL)

