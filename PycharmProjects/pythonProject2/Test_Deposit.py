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

        browser.get('https://s-u-p.zabbet168.com/th/auth/login')

        username = browser.find_element(By.NAME, 'username')
        username.send_keys('admin000022')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('9v~C3V[CEf&HDcY^')
        password.submit()

        print("[{}] Login !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(100)

        Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button/div').click()
        Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul')
        all_option = Edit_bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        time.sleep(2)

        Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H:%M %p")))

        time.sleep(100)

        Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(100000)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[2]/input')
        Search.send_keys('1013000000')

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
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H:%M %p")))

        time.sleep(2)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบสร้างรายการฝาก')

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Bill Number successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Bill Number false !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        A_2 = 100
        print('[{}] Approve Deposit Bill Number 100฿ !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login password !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1013000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password005')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        print('[{}] User create deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/button/span').click()

        time.sleep(3)

        NoPro = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/button[2]').click()

        try:

            time.sleep(3)

            money = browser.find_element(By.ID, 'deposit-amount')
            money.send_keys('100')
            money.submit()

            time.sleep(5)

            print('[{}] User create deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] User create deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(3)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[2]/input')
        Search.send_keys('1013000000')

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button[1]')
        Search.click()

        time.sleep(2)

        Approve = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        Approve.click()

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Upload Slip successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Upload Slip false !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        A_3 = 100
        print('[{}] Approve Deposit Upload Slip 100฿ !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(20)

        Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button/div').click()
        Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul')
        all_option = Edit_bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H:%M %p")))

        time.sleep(1)

        Promotion1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[11]/div/div[2]').click()
        Promotion2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[11]/div/div[3]/ul/li[2]').click()
        print('[{}] promotion ฝากน้อย ได้เยอะ !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        time.sleep(1)

        Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/div[2]/input')
        Search.send_keys('1013000000')

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
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H:%M %p")))
        print(Time)

        time.sleep(2)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบสร้างรายการฝาก')

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:
            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Bill Number successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
