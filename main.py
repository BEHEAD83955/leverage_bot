from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
from queue import Queue

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"
bot = Bot(token=TOKEN)

app = Flask(__name__)

# 新增 queue 給 Dispatcher 使用
update_queue = Queue()
dispatcher = Dispatcher(bot, update_queue, workers=0, use_context=True)

# /start 指令的處理器
def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Bot 已啟動，請輸入代碼進行計算。")

dispatcher.add_handler(CommandHandler("start", start))

# Telegram Webhook 的處理
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Render 檢查用
@app.route("/")
def index():
    return "Bot is running"
