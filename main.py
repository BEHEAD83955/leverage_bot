from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import os

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# /start 指令
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot 已啟動")

dispatcher.add_handler(CommandHandler("start", start))

app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <-- 重點：Render 會給你 PORT
    app.run(host="0.0.0.0", port=port)
