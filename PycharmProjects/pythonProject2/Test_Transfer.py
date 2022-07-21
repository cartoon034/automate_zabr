from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_number import random_number_num_generator
from random_username.generate import generate_username
from random_phone import random_phone_num_generator
from selenium.webdriver.support.select import Select
from random import randint

import random
import datetime
import time
import sys


if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    try:

        time.sleep(1)

        print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(1)

        username = browser.find_element(By.NAME, 'username')
        username.send_keys('admin000022')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('9v~C3V[CEf&HDcY^')
        password.submit()

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Transfer !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        def Create_Transfer():

            


            print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)