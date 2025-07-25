import telebot

# 替換成你的真實 Token
API_TOKEN = '7929780148:AAEKw3t9XUQdc-LkxK2J9tCWwbxqMtahjoU'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 歡迎使用槓桿倉位計算機！\n請輸入指令格式：/calc 入場價 倉位大小\n例如：/calc 62000 1000")

@bot.message_handler(commands=['calc'])
def calc_handler(message):
    try:
        _, price_str, target_str = message.text.split()
        entry_price = float(price_str)
        position_size = float(target_str)

        result = f"📊 入場價：{entry_price:.2f} USDT\n🎯 目標倉位：{position_size:.2f} USDT\n\n"
        for leverage in range(1, 26):
            margin = position_size / leverage
            contracts = position_size / entry_price
            result += f"🔹{leverage}x 槓桿 → 保證金: {margin:.2f} USDT｜張數: {contracts:.4f} BTC\n"

        bot.reply_to(message, result)
    except:
        bot.reply_to(message, "⚠️ 請使用正確格式：/calc 入場價 倉位大小\n例如：/calc 62000 1000")

bot.polling()
