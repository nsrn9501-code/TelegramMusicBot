from flask import Flask
from telebot import TeleBot, types
import os

app = Flask(__name__)

# التوكن يتم قراءته من متغير بيئي داخل Railway
TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

@app.route('/')
def home():
    return "بوت نصر شغال ✅"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت نصر! أرسل رابط فيديو من يوتيوب لتحميله 🎧")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        bot.reply_to(message, f"جاري تحميل الفيديو من:\n{url}")
        # لاحقًا تقدر تضيف كود yt-dlp هنا
    else:
        bot.reply_to(message, "أرسل رابط يوتيوب فقط 🎬")

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080)).start()
    bot.polling()
