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

        print("[{}] Login Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Add_user = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        browser.execute_script("arguments[0].click();", Add_user)

        print('[{}] create user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Phone_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[1]/div[2]/input')
        Phone_number.send_keys('1012000000')

        Gender = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div[2]/fieldset/div/div/div[3]/input').click()

        First_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
        First_name.send_keys('test the')

        Last_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/input')
        Last_name.send_keys('system')

        User_group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[3]/ul/li[1]').click()

        Affiliate_Group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[1]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[1]').click()

        Commission_Group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[7]/div[2]/div/div[1]').click()

        Commission_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[7]/div[2]/div/div[3]/ul/li[1]').click()
        # time.sleep(2)
        Bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/button[2]').click()
        Bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/ul')
        all_option = Bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[9]/div[2]/input')
        Account_name.send_keys('test the system')

        Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[10]/div[2]/input')
        Account_number.send_keys('1012000000')

        Password = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[11]/div[2]/input')
        Password.send_keys('password009')

        Remark = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[12]/div[2]/div/textarea')
        Remark.send_keys('test the system')

        time.sleep(2)

        Save = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(3)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] create user successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] create user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login user!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1012000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password009')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(3)

            profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


        time.sleep(3)

        deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/button/span').click()

        time.sleep(3)

        NoPro = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/button[2]').click()

        try:

            time.sleep(3)

            money = browser.find_element(By.ID, 'deposit-amount')
            money.send_keys(randint(1, 10000))
            money.submit()

            time.sleep(5)

            cancel = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/div/div[7]/button').click()

            print('[{}] deposit successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        profile = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

        time.sleep(2)

        logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        time.sleep(5)

        print('[{}] logout !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1012000000')
        Search.submit()

        print("[{}] Search !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        Edit_user2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Edit_user2)

        print('[{}] Edit user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        First_name_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/input')
        First_name_clear.clear()

        First_name = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/input')
        First_name.send_keys('ทดสอบ')

        Last_name_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        Last_name_clear.send_keys(Keys.CONTROL + "a")

        Last_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        Last_name.send_keys('ทดสอบ')

        User_group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/div/div[3]/ul/li[2]').click()

        Affiliate_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[2]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[2]').click()

        Commission_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[2]').click()

        Commission_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[3]/ul/li[2]').click()

        Remark = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/textarea')
        Remark.send_keys('ทดสอบ')

        Save = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]').click()

        time.sleep(2)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] Edit user successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        print('[{}] Edit password !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_password = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", Edit_password)

        password1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/input')
        password1.send_keys('password005')

        confirm_password = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/input')
        confirm_password.send_keys('password005')

        Save2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]').click()

        time.sleep(1)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] password successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login password old  !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1012000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password009')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(3)

            profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login password successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        print('[{}] login password new!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys(Keys.CONTROL + "a")

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1012000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys(Keys.CONTROL + "a")

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password005')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login password successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        time.sleep(5)

        print('[{}] logout !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1012000000')
        Search.submit()

        print("[{}] Search !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print("[{}] Edit bank !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Edit_bank = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[3]/a/div')
        browser.execute_script("arguments[0].click();", Edit_bank)

        time.sleep(2)

        Edit_bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/div[2]/button[2]').click()
        Edit_bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/div[2]/ul')
        all_option = Edit_bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        time.sleep(2)

        Account_name = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/input')
        Account_name.clear()

        Account_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/input')
        Account_name.send_keys('นารา มาสาย')

        time.sleep(2)

        Account_number = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div/div/input')
        Account_number.clear()

        Account_number = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div/div/input')
        Account_number.send_keys('1234567890')

        Approve_Now = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/div/div[1]/button').click()

        time.sleep(1)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Edit bank successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit bank false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))



        time.sleep(10000)

        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
