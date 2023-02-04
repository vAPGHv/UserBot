from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def yarus(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(800, 800)

        old_num = phone_num
        phone_num = phone_num[2:]

        driver.get("https://yarus.ru/auth")

        sleep(1)

        driver.find_element(By.XPATH, "//input[@class=\"base-input__field common-input__field\"]").send_keys(phone_num)
        driver.find_element(By.XPATH, "//label[@class=\"base-checkbox\"]").click()

        sleep(0.2)

        driver.find_element(By.XPATH, "//button[@class=\"base-button base-button_type_primary base-button_subtype_default base-button_size_large base-button_full-width auth-screen-entry__button\"]").click()

        print(old_num, "yarus completed!")
    except Exception as ex:
        driver.save_screenshot("yarus/screen.png")
        print(old_num, "yarus err!")
    finally:
        driver.quit()
