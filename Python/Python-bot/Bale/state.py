from balethon import Client
from balethon.objects import Message
from balethon.conditions import at_state
import env

bot = Client(token=env.TOKEN)

@bot.on_command(at_state(None), name='start')
async def start(*, message: Message):
    await message.reply('خوش اومدی! اسمت چیه؟')
    message.author.set_state('wait_first_name')

@bot.on_message()
async def all_steps(*, message: Message):
    state = message.author.get_state()
    text = message.text.strip()

    # مرحله 1: نام دریافت شده، منتظر فامیلی هستیم
    if state and state.startswith('wait_last_name|'):
        _, first_name = state.split('|', 1)
        await message.reply('ممنون! حالا سنت چنده؟')
        message.author.set_state(f'wait_age|{first_name}|{text}')

    # مرحله 2: نام و فامیل دریافت شده، منتظر سن هستیم
    elif state and state.startswith('wait_age|'):
        _, first_name, last_name = state.split('|', 2)
        await message.reply(f'ثبت شد! \nنام: {first_name} {last_name} \nسن: {text}')
        message.author.set_state(None)
    
    # مرحله 3: وضعیت اولیه که توسط start ست شده
    elif state == 'wait_first_name':
        await message.reply('خیلی خب! حالا فامیلت چیه؟')
        message.author.set_state(f'wait_last_name|{text}')




if __name__ == '__main__':
    print('bot start...')
    bot.run()
