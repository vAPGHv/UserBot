from copy import deepcopy as copy
from math import sqrt
import random

from pyrogram import Client, filters  # bot
import asyncio

from time import sleep

from threading import Thread


from fun._fun_info import fun_info_f
from fun.hack import hack_f
from fun.hack import nohack_f
from fun.inp import inp_f
from fun.spam import spam_f

from useful._useful_info import useful_info_f
from useful.bomb import bomb_f
from useful.calc import calc_f

from hacker._hacker_info import hacker_info_f

api_id = 18812221
api_hash = "4b3a8a5527fe075019839f457f2c6dbc"

app = Client("max", api_id=api_id, api_hash=api_hash)  # , phone_number=phone_number, password=password)

print(f"Session name: {app.session_name}")


# ===============FUN FUNCTIONS===============
@app.on_message(filters.command("hack", prefixes="/") & filters.me)  # command
async def hack(_, msg):
    await hack_f(app, msg)
@app.on_message(filters.command("nohack", prefixes="/") & filters.me)  # command
async def nohack(_, msg):
    await nohack_f(app, msg)
@app.on_message(filters.command("inp", prefixes="/") & filters.me)  # command
async def inp(_, msg):
    await inp_f(app, msg)
@app.on_message(filters.command("spam", prefixes="/") & filters.me)  # command
async def spam(_, msg):
    await spam_f(app, msg)

# ===============USEFUL FUNCTIONS===============
@app.on_message(filters.command("calc", prefixes="/") & filters.me)  # command
async def calc(_, msg):
    await calc_f(app, msg)
@app.on_message(filters.command("bomb", prefixes="/") & filters.me)  # command
async def bomb(_, msg):
    await bomb_f(app, msg)

# ===============INFO FUNCTIONS===============
@app.on_message(filters.command('useful', prefixes="/") & filters.me)  # command
async def useful_info(_, msg):
    await useful_info_f(app, msg)
@app.on_message(filters.command('fun', prefixes="/") & filters.me)  # command
async def fun_info(_, msg):
    await fun_info_f(app, msg)
@app.on_message(filters.command('hacker', prefixes="/") & filters.me)  # command
async def hacker_info(_, msg):
    await hacker_info_f(app, msg)
@app.on_message(filters.command('info', prefixes="/") & filters.me)  # command
async def info(_, msg):
    await msg.edit("""Что бы подробнее узнать о функциях введите 1 из следующих комманд:
    <code>/hacker</code> функции для пентестинга
    <code>/fun</code> функции для развлечений
    <code>/useful</code> полезные функции    
    
    Made by: @vapgsv
    Tester: @real_azart
    Version: 2.11 (04.02.23)
    """, parse_mode="html")

app.run()
