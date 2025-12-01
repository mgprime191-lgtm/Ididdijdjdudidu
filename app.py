import telebot

bot = "8550320213:AAGJiILpko3jKb15O2s3AqE_v1stb1V9ZyA"  # Replace with your token

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "I'm alive 24/7! 🚀")

bot.polling(none_stop=True)  # Keeps the bot running
