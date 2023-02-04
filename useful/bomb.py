from useful.bomber.main import bomber


async def bomb_f(app, msg):
    try:
        data = msg.text.split("/bomb ", maxsplit=1)[1]

        number = data.split(" ")[0]
        iter = data.split(" ")[1]

        bomber(number, iter)

    except Exception as ex:
        await msg.edit(f"Произошла следующая ошибка:\n\n{ex}")