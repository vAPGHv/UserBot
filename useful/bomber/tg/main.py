from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def tg(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(800, 800)

        old_num = phone_num
        phone_num = phone_num[2:]

        driver.get("https://web.telegram.org/k/")

        sleep(1)

        driver.find_element(By.XPATH, "//button[@class=\"btn-primary btn-secondary btn-primary-transparent primary rp\"]").click()

        sleep(1)

        driver.find_elements(By.XPATH, "//div[@class=\"input-field-input\"]")[1].send_keys(phone_num)

        sleep(1)

        driver.find_elements(By.XPATH, "//div[@class=\"input-field-input\"]")[1].send_keys(Keys.ENTER)

        print(old_num, "tg completed!")
    except Exception as ex:
        driver.save_screenshot("tg/screen.png")
        print(old_num, "tg err!")
    finally:
        driver.quit()
