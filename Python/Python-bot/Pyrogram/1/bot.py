from pyrogram import *

app = Client(
    "JobFinderIranBot",
)
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"

TARGET = -4756620381

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [u.mention for u in message.new_chat_members]
    # Build the welcome message by using an emoji and the list we built above
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)


app.run()


app.run()