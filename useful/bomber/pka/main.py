from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def pka(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(800, 800)

        old_num = phone_num
        phone_num = phone_num[2:]

        driver.get("https://id.x5.ru/auth/realms/ssox5id/protocol/openid-connect/auth?client_id=tc5_web&redirect_uri=https://5ka.ru/my&state=uAes6m9RnneF&response_mode=query&response_type=code&scope=openid&nonce=xUkJUimD7mpD")

        sleep(1)

        driver.find_element(By.XPATH, "//*[@id=\"username\"]").send_keys(phone_num)
        driver.find_element(By.XPATH, "//*[@class=\"submit-button btn btn-primary\"]").click()

        print(old_num, "5ka completed!")
    except Exception as ex:
        driver.save_screenshot("pka/screen.png")
        print(old_num, "5ka err!")
    finally:
        driver.quit()
