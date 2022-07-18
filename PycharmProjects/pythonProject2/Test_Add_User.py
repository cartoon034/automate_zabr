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

        time.sleep(1)

        Add_user = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        browser.execute_script("arguments[0].click();", Add_user)

        print('[{}] create user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Phone_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[1]/div[2]/input')
        Phone_number.send_keys('1013000000')

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
        Account_number.send_keys('1013000000')

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

            print('[{}] create user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] create user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] try login user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1013000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password009')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(3)

            profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


        time.sleep(3)

        print('[{}] try User create deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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

            print('[{}] User cancel deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] User cancel deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        profile = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

        time.sleep(2)

        logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        time.sleep(5)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1013000000')
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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
        First_name.send_keys('ชื่อทดสอบ')

        Last_name_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        Last_name_clear.send_keys(Keys.CONTROL + "a")

        Last_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        Last_name.send_keys('นามสกุนทดสอบ')

        User_group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/div/div[3]/ul/li[2]').click()

        Affiliate_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[2]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[2]').click()

        Commission_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[2]').click()

        Commission_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[3]/ul/li[2]').click()

        Remark1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/textarea')
        Remark1.send_keys(Keys.CONTROL + "a")

        Remark2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/textarea')
        Remark2.send_keys('ทดสอบแก้ไขผู้ใช้')

        Save = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]').click()

        time.sleep(2)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] Edit user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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

            print('[{}] Edit password successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] try login user password old  !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1013000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password009')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(3)

            profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user password successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        print('[{}] try login user password new!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys(Keys.CONTROL + "a")

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('1013000000')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys(Keys.CONTROL + "a")

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('password005')

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user password successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        print('[{}] logout user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        time.sleep(5)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('1013000000')
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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

        time.sleep(1)

        Account_name = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/input')
        Account_name.clear()

        Account_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/input')
        Account_name.send_keys('ทดสอบ นะนะ')

        time.sleep(1)

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

            print('[{}] Edit bank successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit bank false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print("[{}] Edit partner !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Edit_partner = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[4]/a/div')
        browser.execute_script("arguments[0].click();", Edit_partner)

        Edit_partner2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/div[2]/div[2]')
        browser.execute_script("arguments[0].click();", Edit_partner2)

        Edit_partner3 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/div[2]/div[3]/ul/li[2]')
        browser.execute_script("arguments[0].click();", Edit_partner3)

        Edit_Remark = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/input')
        Edit_Remark.send_keys('ทดสอบผูกพันธมิตร')

        Save_Edit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]')
        browser.execute_script("arguments[0].click();", Save_Edit)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Edit partner successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit partner false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/button')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print("[{}] Adjust credit !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Adjust_credit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr/td[10]/div/ul/li[5]/a')
        browser.execute_script("arguments[0].click();", Adjust_credit)

        username = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/input')
        username.send_keys(Keys.CONTROL + "a")

        time.sleep(1)

        credit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div/div/input')
        credit.send_keys('100')

        time.sleep(1)

        credit_Remark = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div/div/input')
        credit_Remark.send_keys('ทดสอบเพิ่มเครดิต')

        time.sleep(1)

        Reviewing = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div/div/input')
        Reviewing.click()

        Save = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]')
        browser.execute_script("arguments[0].click();", Save)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Adjust credit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Adjust credit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        A_1 = 100
        print('[{}] djust credit 100฿ !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


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

        Edit_bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button/div').click()
        Edit_bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul')
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

            print('[{}] Approve Deposit Bill Number successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Bill Number false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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

            print('[{}] Approve Deposit Upload Slip successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Upload Slip false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

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

        A_4 = 100
        print('[{}] Approve Deposit Bill Number 100฿ !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(10000)

        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit !".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
