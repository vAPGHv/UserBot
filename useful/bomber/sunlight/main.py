from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager as driver_manager


def sunlight(opts, phone_num):
    try:
        driver = webdriver.Chrome(service=Service(driver_manager().install()), options=opts)
        driver.set_window_size(1100, 1100)

        old_num = phone_num

        phone_num = list(phone_num)
        phone_num.insert(2, " (")
        phone_num.insert(6, ") ")
        phone_num.insert(-2, "-")
        phone_num.insert(-5, "-")

        phone_num = "".join(phone_num)

        driver.get("https://sunlight.net/profile/login/?next_encoded=Lw==")

        sleep(1)

        inp = driver.find_element(By.XPATH, "//input[@class=\"input input-phone\"]")
        inp.send_keys(phone_num)

        sleep(1)

        button = driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
        button.click()

        print(old_num, "sunlight completed!")
    except Exception as ex:
        driver.save_screenshot("sunlight/screen.png")
        print(old_num, "sunlight err!")
    finally:
        driver.quit()
