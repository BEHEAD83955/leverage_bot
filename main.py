from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = "7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("嗨！攝影師倉位BOT 啟動成功📸")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()
