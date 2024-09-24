# @ReshalaNeBot
import telebot, requests, json, random

TOKEN = '6003616188:AAHNSNaSKt_vMm92BQeM38tQEobkeMtZWEk'

bot = telebot.TeleBot(TOKEN)

data = {}


def makeSession(id):
    global data
    if id in data:
        return
    
    data[id] = {}
    data[id]["heaps"], data[id]["maxHeapSize"], data[id]["turn"] = 3, 10, 0
    data[id]["lastHeaps"], data[id]["curHeaps"] = [], []
    data[id]["lastXor"], data[id]["curXor"], data[id]["curTurn"] = -1, 0, 0
    data[id]["isPlaying"] = False
    data[id]["chosenHeap"] = -1


@bot.message_handler(commands=['start'])
def start_messages(message):
    text = "Что-то началось!"
    bot.send_message(message.from_user.id, text=text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global data
    id = message.from_user.id
    makeSession(id)

    print(message.json['text'])

    #ret = f'Поздравляю, Вы умеете писать.\n Сильно сказано:\n
    #    { message. }'
    bot.send_message(message.from_user.id, f'Поздравляю, Вы умеете писать.\nСильно сказано: \
                     "{message.json["text"]}"')


bot.infinity_polling()