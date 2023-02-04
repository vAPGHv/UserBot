from time import sleep


async def hack_f(app, msg):
    non = "░"
    load = [non] * 10
    loadnum = 0
    text = msg.text.split("/hack ")[1]

    time, name = text.split(" ", maxsplit=1)  # get the time and word after the command

    for i in range(0, 100):
        try:

            if loadnum < 10:
                load[loadnum] = "█"
                loadnum += 1
            else:
                loadnum = 0

            await msg.edit(f"Взлом объекта {name} в процессе... {i}%\n[{''.join(load)}]")
            if loadnum < 10:
                load[loadnum - 1] = non
            else:
                load[9] = non
            sleep(float(time))

        except:
            sleep(0.1)

    await msg.edit(f"Взлом объекта '{name}' в процессе... 100%\n [██████████] \nОбъект {name} был взломан!")

async def nohack_f(app, msg):
    non = "░"
    load = [non] * 10
    loadnum = 0
    text = msg.text.split("/nohack ")[1]

    time, name = text.split(" ", maxsplit=1)  # get the time and word after the command

    for i in range(0, 100):
        try:

            if loadnum < 10:
                load[loadnum] = "█"
                loadnum += 1
            else:
                loadnum = 0

            await msg.edit(f"Взлом объекта {name} в процессе... {i}%\n[{''.join(load)}]")
            if loadnum < 10:
                load[loadnum - 1] = non
            else:
                load[9] = non
            sleep(float(time))

        except:
            sleep(0.1)

    await msg.edit(f"Взлом объекта '{name}' в процессе... 100%\n [██████████] \nОбъект {name} не был взломан!")
