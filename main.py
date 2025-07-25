from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"
bot = Bot(token=TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

# 處理 /start 指令
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot 已啟動")

dispatcher.add_handler(CommandHandler("start", start))

# webhook 接收處理
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# ✅ 關鍵：host="0.0.0.0"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
