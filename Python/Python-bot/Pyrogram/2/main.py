from pyrogram import *
import config
import re

app = Client('SingBot', api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.TOKEN ,app_version="0.1")

sing_state = {}
pattern = r'^[آ-ی ]+$'


@app.on_message(filters.command('start'))
async def start(client, message):
    user_id = message.from_user.id
    
    await app.send_message(chat_id=message.chat.id, text='درود خوش اومدی به ربات ثبت نام\n اسم کامل خودتو وارد کن')

    sing_state[user_id] = {'step': "waiting_name"}

    print(sing_state)

@app.on_message(filters.text & filters.private)
async def handle_text(client, message):

    user_id = message.from_user.id
    user_answer = message.text
    user_answer = user_answer.strip()

    if user_id in sing_state:
        state = sing_state[user_id]

        if state["step"] == 'waiting_name':
            if len(user_answer) <= 6:
                await app.send_message(chat_id=message.chat.id, text='لطفا اسم و فامیل را کامل وارد کنید')
                sing_state[user_id] = {'step': "waiting_name"}
                return  
            elif not re.fullmatch(r'^[آ-ی ]+$', user_answer):
                await app.send_message(chat_id=message.chat.id, text='لطفا از وارد کردن علامت و عدد خودداری کنید')
                sing_state[user_id] = {'step': "waiting_name"}
                return  
            else:
                await app.send_message(chat_id=message.chat.id, text='حالا سن خودتو وارد کن')
                sing_state[user_id] = {'step': 'waiting_age'}
                return  
            
        elif state["step"] == 'waiting_age':

            if not user_answer.isdigit():
                await app.send_message(chat_id=message.chat.id, text='لطفا سن خود را به عدد صحیح وارد کنید')
                sing_state[user_id] = {'step': 'waiting_age'}
                return
            else:
                sing_state[user_id] = {'step': 'waiting_done'}
                await app.send_message(chat_id=message.chat.id,
                                    text='درود! آیا از ثبت نام راضی هستید؟ لطفا "بله" یا "خیر" وارد کنید')
                return
 
            
        elif state["step"] == 'waiting_done':
            if user_answer == 'بله':
                await app.send_message(chat_id=message.chat.id, text="ممنونم از بازخورد")
                sing_state.pop(user_id)
            elif user_answer == 'خیر':
                await app.send_message(chat_id=message.chat.id, text="برای ثبت نام دوباره /start بزنید")
                sing_state.pop(user_id)
            else:
                await app.send_message(chat_id=message.chat.id, text="لطفا فقط 'بله' یا 'خیر' وارد کنید")


print('bot start...')
app.run()