from math import sqrt
from copy import deepcopy as copy


async def calc_f(app, msg):
    try:
        text = msg.text.split("/calc ", maxsplit=1)[1]

        old_text = copy(text).replace("к", "000").replace("К", "000").replace("k", "000").replace("K", "000").replace(" ", "")

        text = old_text.replace(":", "/").replace("x", "*").replace("х", "*").replace("÷", "/")

        text = eval(text)

        if text == int(text):
            text = int(text)

        await msg.edit(f"{old_text}={text}")
    except Exception as ex:
        await msg.edit(f"Произошла следующая ошибка:\n\n{ex}")
        print()
