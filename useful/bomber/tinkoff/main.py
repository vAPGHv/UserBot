from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def tinkoff(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(800, 800)

        driver.get("https://www.tinkoff.ru/cards/debit-cards/tinkoff-black/?dco_ic=39a2b65d-9296-11ed-8000-00004181259c&utm_term=tcpa&utm_medium=agnt.utl&utm_source=plaksickiievgeniiurevich1_tb&utm_campaign=debit.black_109&tcpa_click_id=3946e2d0929611eda943066be28bbc0bf55179e05d0849339f1ef9c1b77ea4f5&offer_id=109&cookie_exp=1440")

        sleep(1)

        driver.find_element(By.XPATH, "//div[@class=\"ebSRvPGaa\"]").click()

        sleep(1)

        driver.find_element(By.XPATH, "//input[@id=\"phoneNumber\"]").send_keys(phone_num)
        driver.find_element(By.XPATH, "//button[@class=\"ui-button\"]").click()

        print(phone_num, "tinkoff completed!")
    except Exception as ex:
        driver.save_screenshot("tinkoff/screen.png")
        print(phone_num, "tinkoff err!")
    finally:
        driver.quit()
