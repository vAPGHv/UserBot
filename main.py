# ru:
# когда попросят ввести phone number вводите номер телефона и нажмите enter (а потом код который прийдёт и снова enter)
# api_id и api_hash (в config.ini) можно узнать тут: https://my.telegram.org/auth
# должен быть установлен пайтон, и модули pyrogram, requests и bs4
# бот работает во всех чатах где есть вы!

"""
en:
when asked to enter a phone number, enter the phone number and press enter (and then the code that comes and enter again)
api_id and api_hash (in config.ini) can be found here: https://my.telegram.org/auth
python must be installed, and pyrogram, requests and bs4 modules
bot works in all chats where you are!
"""

# -------=imports=-------
from pyrogram import Client, filters  # bot
from time import sleep
import requests as req
from bs4 import BeautifulSoup as BS
import random
import pyttsx3

api_id = 
api_hash = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("say", prefixes="/") & filters.me)  # command
async def say(_, msg):
    slt = msg.text.split("/say ")[1]

    engine = pyttsx3.init()
    engine.save_to_file(slt, "say.mp3")
    engine.runAndWait()

    x = 1

    if x == 1:
        await msg.reply_audio("say.mp3")

    await msg.delete()


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
    reg = msg.text.split("/img ")[1]  # get the word after the command
    url = f"https://www.google.com/search?q={reg}&client=opera&hs=nkI&hl=ru&sxsrf=APq-WBuUWCpyLYYduHWl9vqF9dG_IIvdpg:1649445742756&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizzsqcmIX3AhVM-yoKHcKBCg0Q_AUoAXoECAEQAw&biw=2519&bih=1299&dpr=1"

    r = req.get(url)

    soup = BS(r.content, "html.parser")
    list1 = []

    for i in soup.select("img", class_="Q4LuWd"):
        list1.append(i.get("src"))

    randel = list1[random.randrange(1, len(list1))]
    randel = req.get(randel).content

    with open(f"123.jpg", "wb") as file:
        file.write(randel)

    await msg.reply_photo("123.jpg")


# img and delete msg
@app.on_message(filters.command("dimg", prefixes="/") & filters.me)  # command
async def img(_, msg):
    reg = msg.text.split("/dimg ")[1]  # get the word after the command
    url = f"https://www.google.com/search?q={reg}&client=opera&hs=nkI&hl=ru&sxsrf=APq-WBuUWCpyLYYduHWl9vqF9dG_IIvdpg:1649445742756&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizzsqcmIX3AhVM-yoKHcKBCg0Q_AUoAXoECAEQAw&biw=2519&bih=1299&dpr=1"

    r = req.get(url)

    soup = BS(r.content, "html.parser")
    list1 = []

    for i in soup.select("img", class_="Q4LuWd"):
        list1.append(i.get("src"))

    randel = list1[random.randrange(1, len(list1))]
    randel = req.get(randel).content

    with open(f"123.jpg", "wb") as file:
        file.write(randel)

    await msg.reply_photo("123.jpg")
    await msg.delete()


@app.on_message(filters.command("spam", prefixes="/") & filters.me)  # command
async def reverse(_, msg):
    slt = msg.text.split("/spam ")[1]

    slt = slt.split(" ")[0]
    text = msg.text.split(f"/spam {slt} ", maxsplit=1)[1]  # get the word after the command

    for i in range(0, int(slt)):
        await msg.reply(text)

    await msg.delete()


@app.on_message(filters.command('info', prefixes="/") & filters.me)  # command
async def info(_, msg):
    await msg.edit("""Вот что я могу:
    /hack 0.2 эффект хакинг
    /nohack 0.2 эффект хакинг (неудача)
    /inp 0.05 ввод текста
    /rev переворот текста
    /img отправка изображений по запросу
    /dimg отправка изображений по запросу с удалением сообщения
    /spam 5 спам
    /say текст воспроизводит звук текста
    
    Made by: @vapgsv
    Version: 1.2
    """)


app.run()
