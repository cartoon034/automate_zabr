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

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1013200000')
        Search.submit()

        time.sleep(2)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(100)

        time.sleep(1)

        Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
        Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[4]/a').click()

        time.sleep(3)

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        time.sleep(2)

        Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H:%M %p")))

        time.sleep(1)

        Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[13]/input')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        time.sleep(10000)

        Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        time.sleep(1)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[2]/input')
        Search.send_keys('1013200000')

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button[1]')
        Search.click()

        time.sleep(2)

        Approve = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        Approve.click()

        Approve2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div/button')
        Approve2.click()

        Date = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("121212")))

        time.sleep(2)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบสร้างรายการฝาก')

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Bill Number successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Bill Number false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1013200000')
        Search.submit()

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH,  '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(100)

        time.sleep(1)

        Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
        Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[4]/a').click()

        time.sleep(3)

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        time.sleep(2)

        Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("121212")))

        time.sleep(1)

        Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[13]/input')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        time.sleep(1)

        Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        time.sleep(100000)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[2]/input')
        Search.send_keys('1013200000')

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button[1]')
        Search.click()

        time.sleep(2)

        Approve = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        Approve.click()

        Approve2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div/button')
        Approve2.click()

        Date = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("121212")))

        time.sleep(2)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบสร้างรายการฝาก')

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(10000)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Bill Number successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Bill Number false !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
