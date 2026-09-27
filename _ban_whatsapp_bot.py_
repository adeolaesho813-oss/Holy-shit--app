import os
import requests
import telebot

# Telegram Bot Token
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Whatsapp URL for permanent ban
BAN_URL = "https://web.whatsapp.com/fix-ban"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Type /ban to permanently ban Whatsapp.")

@bot.message_handler(commands=["ban"])
def ban_whatsapp(message):
    # Send GET request to ban URL
    try:
        response = requests.get(BAN_URL, timeout=5)
        if response.status_code == 200:
            bot.reply_to(message, "Whatsapp banned successfully.")
        else:
            bot.reply_to(message, f"Failed to ban. Status: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"Error banning: {e}")

# Start the bot
if __name__ == "__main__":
    print("Bot started. Waiting for commands...")
    bot.polling()
