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

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(1)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Add_user = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        browser.execute_script("arguments[0].click();", Add_user)

        Phone_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[1]/div[2]/input')
        Phone_number.send_keys('1900000000')

        First_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        First_name.send_keys('test the')

        Last_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
        Last_name.send_keys('system')

        User_group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/div/div[3]/ul/li[10]').click()

        Affiliate_Group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[1]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[3]/ul/li[3]').click()

        Commission_Group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[1]').click()

        Commission_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[6]').click()
        # time.sleep(2)
        Bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/button[2]').click()
        Bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/ul')
        all_option = Bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[8]/div[2]/input')
        Account_name.send_keys('test the system')

        Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[9]/div[2]/input')
        Account_number.send_keys('1900000000')

        Password = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[10]/div[2]/input')
        Password.send_keys('password01')

        Remark = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[11]/div[2]/div/textarea')
        Remark.send_keys('test the system')

        time.sleep(3000)

        Save = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(2)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] create user successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] create user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys('0000000090')
        Search.submit()

        print("[{}] Search !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/table/tbody/tr[1]/td[10]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        First_name_clear = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[2]/div/div/input')
        First_name_clear.clear()

        First_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[2]/div/div/input')
        First_name.send_keys('')

        Last_name_clear = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[3]/div/div/input')
        Last_name_clear.clear()

        Last_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[3]/div/div/input')
        Last_name.send_keys('มาสาย')

        User_group = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[4]/div/div/select')
        all_option = User_group.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        Password = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div/div[1]/div/div[5]/div/div/input')
        Password.send_keys('pp100200')
        Password.send_keys(Keys.ENTER)

        time.sleep(1)

        Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        Close.send_keys(Keys.ENTER)

        print("[{}] Edit user !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_bank = browser.find_element(By.XPATH,'//*[@id="__BVID__122"]/tbody/tr/td[4]/ul/li[2]/a/i')
        browser.execute_script("arguments[0].click();", Edit_bank)

        Bank = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div/div[1]/div/div[1]/div/div/select')
        Bank.find_element_by_xpath("//option[@value='3']").click()

        Account_name_clear = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div/div[1]/div/div[2]/div/div/input')
        Account_name_clear.clear()

        Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div/div[1]/div/div[2]/div/div/input')
        Account_name.send_keys('นารา มาสาย')

        Account_number_clear = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div/div[1]/div/div[3]/div/div/input')
        Account_number_clear.clear()

        Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div/div[1]/div/div[3]/div/div/input')
        Account_number.send_keys('1234567890')
        Account_number.send_keys(Keys.ENTER)

        time.sleep(1)

        Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        browser.execute_script("arguments[0].click();", Close)

        print("[{}] Edit bank !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Status_ban = browser.find_element(By.XPATH, '//*[@id="__BVID__122"]/tbody/tr/td[4]/ul/li[3]/a/i')
        browser.execute_script("arguments[0].click();", Status_ban)

        time.sleep(1)

        Confirm_ban = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        browser.execute_script("arguments[0].click();", Confirm_ban)

        time.sleep(1)

        Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        browser.execute_script("arguments[0].click();", Close)

        print("[{}] Status ban !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Delete_user = browser.find_element(By.XPATH, '//*[@id="__BVID__122"]/tbody/tr/td[4]/ul/li[4]/a/i')
        browser.execute_script("arguments[0].click();", Delete_user)

        Confirm_delete = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        Confirm_delete.send_keys(Keys.ENTER)

        time.sleep(1)

        Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        Close.send_keys(Keys.ENTER)

        print("[{}] Delete user !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
