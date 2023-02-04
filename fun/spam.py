from time import sleep


async def spam_f(app, msg):
    try:
        text = msg.text.split("/spam ", maxsplit=1)[1]

        amount, text = text.split(" ", maxsplit=1)  # get the time and word after the command

        for i in range(0, int(amount)):
            await msg.reply(text)

        await msg.delete()
    except:
        sleep(0.1)
