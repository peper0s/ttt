import telebot
from random import randint
from keras1 import AI

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, '''привет!
/start - запустить бота
/help - информация о командах
/random - генерация случайного числа
                 ''')

@bot.message_handler(commands=['random'])
def number(message):
    x = randint(1, 1000)
    bot.reply_to(message, str(x)) 
    bot.send_message(message.chat.id, str(x))


# сделать команду, которая скачивает картинку, которую отправил пользователь (документация, google)
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:

        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

       #pandas.read_csv(r'C:\Users\Grinkevich Tim\Documents\ttt.csv')+file_info.file_path;
        
        name = file_info.file_path.split('/')[-1]
        with open(f'images/{name}', 'wb') as new_file:
           new_file.write(downloaded_file)
        
        bot.reply_to(message,"Фото добавлено, идет распозанвание") 
        
        result = AI(f'images/{name}')
        bot.reply_to(message, result)
        #1 о,учить модель
        #2 вернуть процент распознавания
       

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()