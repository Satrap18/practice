from pyrogram import filters

# ذخیره وضعیت هر کاربر
user_state = {}

def setup_handlers(app):

    @app.on_message(filters.command("start"))
    async def start_text(client, message):

        user_id = message.from_user.id

        # مقدار اولیه state کاربر
        user_state[user_id] = {
            "step": "num1",
            "num1": None,
            "sigh": None,
            "num2": None
        }

        await client.send_message(
            message.chat.id,
            "درود، خوش اومدی.\nعدد اول را بفرست:"
        )

    @app.on_message(filters.text & ~filters.command("start"))
    async def calculator_handler(client, message):

        user_id = message.from_user.id
        chat_id = message.chat.id
        text = message.text.strip()

        # اگر کاربر هنوز /start نزده باشد
        if user_id not in user_state:
            user_state[user_id] = {
                "step": "num1",
                "num1": None,
                "sigh": None,
                "num2": None
            }
            await client.send_message(chat_id, "عدد اول را بفرست:")
            return

        state = user_state[user_id]

        # ۱. دریافت num1
        if state["step"] == "num1":
            if not text.isdigit():
                await client.send_message(chat_id, "لطفاً یک عدد معتبر بفرست.")
                return

            state["num1"] = int(text)
            state["step"] = "sigh"

            await client.send_message(chat_id, "عملیات را بفرست (+ - * /):")
            return

        # ۲. دریافت sigh
        elif state["step"] == "sigh":
            if text not in ["+", "-", "*", "/"]:
                await client.send_message(chat_id, "لطفاً فقط یکی از این‌ها را بفرست: + - * /")
                return

            state["sigh"] = text
            state["step"] = "num2"

            await client.send_message(chat_id, "عدد دوم را بفرست:")
            return

        # ۳. دریافت num2 و محاسبه
        elif state["step"] == "num2":
            if not text.isdigit():
                await client.send_message(chat_id, "عدد دوم معتبر نیست، دوباره بفرست:")
                return

            state["num2"] = int(text)

            num1 = state["num1"]
            sigh = state["sigh"]
            num2 = state["num2"]

            # محاسبه
            if sigh == "+":
                result = num1 + num2
            elif sigh == "-":
                result = num1 - num2
            elif sigh == "*":
                result = num1 * num2
            elif sigh == "/":
                if num2 == 0:
                    result = "خطا: تقسیم بر صفر مجاز نیست."
                else:
                    result = num1 / num2

            # ارسال نتیجه
            await client.send_message(chat_id, f"نتیجه: {result}")

            # ریست state برای استفاده دوباره
            user_state[user_id] = {
                "step": "num1",
                "num1": None,
                "sigh": None,
                "num2": None
            }

            await client.send_message(chat_id, "برای محاسبه جدید، عدد اول را بفرست.")
            return