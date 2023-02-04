from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def yandex(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(800, 800)

        old_num = phone_num
        phone_num = phone_num[2:]

        driver.get("https://passport.yandex.ru/registration")

        sleep(1)

        driver.find_element(By.XPATH, "//input[@id=\"firstname\"]").send_keys("Ишак")
        driver.find_element(By.XPATH, "//input[@id=\"lastname\"]").send_keys("Инвалидович")
        driver.find_element(By.XPATH, "//input[@id=\"login\"]").send_keys("sfdnjdkhsjks")
        driver.find_element(By.XPATH, "//input[@id=\"password\"]").send_keys("Ishaq_Polosatov_Invalidovich")
        driver.find_element(By.XPATH, "//input[@id=\"password_confirm\"]").send_keys("Ishaq_Polosatov_Invalidovich")
        driver.find_element(By.XPATH, "//input[@id=\"phone\"]").send_keys(phone_num)

        driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()

        print(old_num, "yandex completed!")
    except Exception as ex:
        driver.save_screenshot("yandex/screen.png")
        print(old_num, "yandex err!")
    finally:
        driver.quit()
