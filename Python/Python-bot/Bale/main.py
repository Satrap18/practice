from balethon import Client
from balethon.objects import Message, ReplyMarkup, ReplyKeyboard, ReplyKeyboardButton, ReplyKeyboardRemove
from balethon.conditions import group
import env

TOKEN = env.TOKEN

bot = Client(token=TOKEN)

@bot.on_message(group)
async def start(*, message: Message):

    if message.text == 'salam':
        await message.reply('salam')
        
        markup = ['test', 'test2']
        await ReplyMarkup(['test'])

if __name__ == "__main__":
    print('Bot Start...')
    bot.run()