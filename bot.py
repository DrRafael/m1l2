from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

bot1 = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """Привет! Я умею отвечать на твои сообщения, а еще реагировать на команды:
                 /help
                 /start
                 /info""")



@bot.message_handler(content_types=['photo'])
def send_info(message):
    bot.reply_to(message, 'Классная фотка')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """Привет! Я умею отвечать на твои сообщения, а еще реагировать на команды:
                 /help
                 /start
                 /info""")


bot.infinity_polling()
