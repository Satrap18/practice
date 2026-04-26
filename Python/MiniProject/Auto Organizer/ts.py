from __future__ import annotations

from tsbot import TSBot, TSCtx, query

bot = TSBot(
    username="serveradmin2",   
    password="",  
    address="5.232.169.195",  
    port=10011,             
    nickname="MySimpleBot", 
    server_id=1,              
)


@bot.on("ready")
async def on_ready(bot: TSBot):
    print("✅ Bot connected and ready!")


@bot.command("ping")
async def ping_command(bot: TSBot, ctx: TSCtx):
    # وقتی تو چت بنویسی: !ping
    await bot.respond(ctx, "pong ✅")


if __name__ == "__main__":
    bot.run()
