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

        Menu_Cash_System = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Menu_Cash_System)

        time.sleep(2)

        Menu_Transfer = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Menu_Transfer)

        time.sleep(2)

        print("[{}] Click Menu Transfer !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Amount_1 = ('100')
        Amount_2 = ('200')

        def Create_Transfer_Bank_1():

            time.sleep(2)

            Withdrawal_Bank1 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/ul/li[1]').click()

            time.sleep(1)

            Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_1)

            Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอทเลือกธนาคารที่ 1 ที่แสดงใน Drop down')

            try:

                time.sleep(2)

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(2)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(2)

                print('[{}] Create Transfer 1 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Transfer 1 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        def Create_Transfer_Bank_2():

            time.sleep(2)

            Withdrawal_Bank1 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/ul/li[2]').click()

            Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_2)

            Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอทเลือกธนาคารที่ 2 ที่แสดงใน Drop down')

            try:

                time.sleep(2)

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(2)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(2)

                print('[{}] Create Transfer 2 successful !'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Transfer 2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        bank_1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_1)

        Create_Transfer_Bank_1()

        bank_1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_1)

        Create_Transfer_Bank_2()


        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)