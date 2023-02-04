from time import sleep


async def inp_f(app, msg):
    text = msg.text.split("/inp ", maxsplit=1)[1]

    time, realtext = text.split(" ", maxsplit=1)  # get the time and word after the command

    text = list(realtext)
    time = float(time) / 2

    num = 0

    text2 = ""

    while len(text) - 1 != num:
        try:
            text2 = text2 + text[num]
            await msg.edit(f"{text2}_")
            num += 1
            sleep(time)
            await msg.edit(f"{text2}")
            sleep(time)
        except:
            sleep(0.1)

    await msg.edit(realtext)