@bot.message_handler(commands=['start']) # 1. Message detect hota hai
def send_welcome(message):
    bot.reply_to(message, "Hello!")      # 2. Bot reply bhejta hai