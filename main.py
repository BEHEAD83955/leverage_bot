import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # 你的 Telegram webhook 處理程式碼
    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # 讀取 Render 給的 PORT
    app.run(host='0.0.0.0', port=port)
