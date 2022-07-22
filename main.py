# -------=imports=-------
from pyrogram import Client, filters  # bot
from time import sleep
import requests as req
from bs4 import BeautifulSoup as BS
import random
from getimg import getimg

api_id = 
api_hash = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("hack", prefixes="/") & filters.me)  # command
async def hack(_, msg):
    non = "░"
    load = [non, non, non, non, non, non, non, non, non, non]
    loadnum = 0
    slt = msg.text.split("/hack ")[1]

    slt = slt.split(" ")[0]
    name = msg.text.split(f"/hack {slt} ", maxsplit=1)[1]  # get the word after the command

    for i in range(0, 100):
        try:

            if loadnum < 10:
                load[loadnum] = "█"
                loadnum += 1
            else:
                loadnum = 0

            await msg.edit(f"Взлом объекта '{name}' в процессе... {i}%\n[{''.join(load)}]")
            if loadnum < 10:
                load[loadnum - 1] = non
            else:
                load[9] = non
            sleep(float(slt))

        except:
            sleep(0.1)

    await msg.edit(f"Взлом объекта '{name}' в процессе... 100%\n [██████████] \nОбъект '{name}' взломан!")


@app.on_message(filters.command("nohack", prefixes="/") & filters.me)  # command
async def nohack(_, msg):
    non = "░"
    load = [non, non, non, non, non, non, non, non, non, non]
    loadnum = 0
    slt = msg.text.split("/nohack ")[1]

    slt = slt.split(" ")[0]
    name = msg.text.split(f"/nohack {slt} ", maxsplit=1)[1]  # get the word after the command

    for i in range(0, 100):
        try:

            if loadnum < 10:
                load[loadnum] = "█"
                loadnum += 1
            else:
                loadnum = 0

            await msg.edit(f"Взлом объекта '{name}' в процессе... {i}%\n[{''.join(load)}]")
            if loadnum < 10:
                load[loadnum - 1] = non
            else:
                load[9] = non
            sleep(float(slt))

        except:
            sleep(0.1)

    await msg.edit(f"Взлом объекта '{name}' в процессе... 100%\n [██████████] \nОбъект '{name}' не был взломан!")


@app.on_message(filters.command("inp", prefixes="/") & filters.me)  # command
async def redact(_, msg):
    slt = msg.text.split("/inp ")[1]

    slt = slt.split(" ")[0]
    realtext = msg.text.split(f"/inp {slt} ", maxsplit=1)[1]  # get the word after the command

    text = list(realtext)

    num = 0

    text2 = ""

    while len(text) - 1 != num:
        try:
            text2 = text2 + text[num]
            await msg.edit(f"{text2}_")
            num += 1
            sleep(float(slt))
        except:
            sleep(0.1)

    await msg.edit(realtext)


@app.on_message(filters.command("rev", prefixes="/") & filters.me)  # command
async def reverse(_, msg):
    text = msg.text.split("/rev ")[1]  # get the word after the command
    await msg.edit(text[::-1])


@app.on_message(filters.command("img", prefixes="/") & filters.me)  # command
async def img(_, msg):
    try:
        reg = msg.text.split("/img ", maxsplit=1)[1]  # get the word after the command

        print(reg)
        getimg(reg)

        await msg.reply_photo("img.jpg")
    except Exception as ex:
        print(ex)
        await msg.edit(ex)


@app.on_message(filters.command("spam", prefixes="/") & filters.me)  # command
async def reverse(_, msg):
    slt = msg.text.split("/spam ")[1]

    slt = slt.split(" ")[0]
    text = msg.text.split(f"/spam {slt} ", maxsplit=1)[1]  # get the word after the command

    for i in range(0, int(slt)):
        await msg.reply(text)

    await msg.delete()


@app.on_message(filters.command("load", prefixes="/") & filters.me)  # command
async def loading(_, msg):
    try:
        slt = msg.text.split("/load ")[1]
        slt = slt.split(" ")[0]

        realtext = msg.text.split(f"/load {slt} ", maxsplit=1)[1]  # get the word after the command

        lsymbols = ["|", "/", "ー", "\\"]  # loading symbols

        for __ in range(25):
            for symbol in lsymbols:
                text = f"{realtext} {symbol}..."
                await msg.edit(text)
                sleep(float(slt))

        await msg.edit(f"{realtext} завершёно!")
    except:
        sleep(0.1)


@app.on_message(filters.command('info', prefixes="/") & filters.me)  # command
async def info(_, msg):
    await msg.edit("""Вот что я могу:
    /hack {t} эффект хакинг
    /nohack {t} эффект хакинг (неудача)
    /inp {t} ввод текста
    /rev переворот текста
    /img отправка изображений по запросу
    /spam {t} спам
    /load {t} процесс
    t - любое время в секундах (например 0.1, 2 и т.д.)
    
    Made by: @vapgsv
    Version: 1.7.2
    """)


app.run()
