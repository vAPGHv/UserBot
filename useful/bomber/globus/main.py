from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def globus(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(1000, 1000)

        old_num = phone_num
        phone_num = phone_num[2:]

        driver.get("https://online.globus.ru/")

        sleep(1)

        driver.find_element(By.XPATH, "//div[@class=\"login_content\"]").click()

        sleep(0.5)

        driver.find_element(By.XPATH, "//*[@id=\"auth-phone\"]").send_keys(phone_num)

        sleep(0.5)

        driver.find_element(By.XPATH, "//*[@id=\"auth-btn-submit\"]").click()

        print(old_num, "globus completed!")
    except Exception as ex:
        driver.save_screenshot("globus/screen.png")
        print(old_num, "globus err!")
    finally:
        driver.quit()
