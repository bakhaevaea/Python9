import telebot
import requests
import time
import random

bot = telebot.TeleBot("5825551453:AAEtyx6sTHQ2M-_QUBcpYNfD_fEHE11g-cY", parse_mode=None)
play = False
number = None
count = 0 

@bot.message_handler(commands=['start', 'help', "hello"])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

  # bot.reply_to(message, message.from_user.first_name)

        
@bot.message_handler(regexp="[ + - / *]" )
def emath_mess(message):
    bot.reply_to(message,eval(str(message.text)))

@bot.message_handler(content_types=["text"])
def hello_user(message):
    global play
    global number
    global count
    if play:
        if message.text.isdigit():
            if int(message.text) > number:
               bot.reply_to(message, "Нет, мое число меньше") 
               count += 1
            elif int(message.text) < number:
                bot.reply_to(message, "Нет, мое число больше") 
                count +=1
            elif int(message.text) == number:
                count +=1
                bot.reply_to(message, f"Ты угадал! С {count} попытки") 
                play = False
                count = 0
        else:
            bot.send_message(message.chat.id, f"Ты не отгадал. Я загадывал число {number}")
            play = False
            count = 0
    else:
        if "привет" in message.text:
            bot.reply_to(message, "Привет"+ message.from_user.first_name)
        
        elif message.text == "играть":

            play = True
            number = random.randint(1,1001)
            bot.reply_to(message, "Отгадай число от 1 до 1000")
        
        elif message.text == "погода":
            r=requests.get("https://wttr.in/?0T")
            print(r.text)
            bot.reply_to(message, r.text)
        
        elif message.text =="котик":
            r=f'https://cataas.com/cat?t=${time.time()}'
            bot.send_photo(message.chat.id, r)
        
        elif message.text =="файл":
            fileTest = open('123.txt',  encoding='utf-8')
            bot.send_document(message.chat.id, fileTest)
            fileTest.close()


        data = open('user_message.txt', 'a+', encoding='utf-8')
        data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
        data.close()


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print("privet")
    data = open('user_message.txt', 'a+', encoding='utf-8')
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()
  
bot.infinity_polling()
