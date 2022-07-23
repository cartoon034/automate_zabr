from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        username.send_keys('admin000033')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('pp100200')
        password.submit()

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        telephone_number = ('0943725983')
        pass_word = ('password005')

        def Create_Deposit():

            time.sleep(3)

            menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
            browser.execute_script("arguments[0].click();", menu_user)

            time.sleep(2)

            menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
            browser.execute_script("arguments[0].click();", menu_user2)

            print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            time.sleep(3)

            Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
            Search.send_keys(telephone_number)
            Search.submit()

            time.sleep(2)

            Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/button')
            browser.execute_script("arguments[0].click();", Edit_user)

            time.sleep(2)

            print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/ul/li[6]')
            Deposit.click()

            time.sleep(2)

            Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
            Amount1.send_keys(Keys.CONTROL + 'a')

            Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
            Amount2.send_keys(100)

            time.sleep(2)

            Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
            Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[4]/a').click()

            time.sleep(3)

            Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
            browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
            Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

            time.sleep(2)

            Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
            browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
            Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H%M%p")))
            # Time.send_keys('121212')

            time.sleep(1)

            Promotions1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[11]/div/div[2]').click()
            Promotions2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[11]/div/div[3]/ul/li[2]').click()

            time.sleep(1)

            Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[13]/input')
            Remark_Deposit.send_keys('บอททดสอบฝากรับโปรโมชั่น')

            time.sleep(1)

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

        def Cancel_Promotions():

            time.sleep(3)

            Promotions = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[6]/a')
            browser.execute_script("arguments[0].click();", Promotions)

            time.sleep(3)

            User_Promotions = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[6]/ul/li[3]/a')
            browser.execute_script("arguments[0].click();", User_Promotions)

            time.sleep(1)

            print('[{}] Click Menu User Promotions !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
            Search.send_keys(telephone_number)
            Search.submit()

            time.sleep(2)

            Concel = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[9]/div/ul/li[2]')
            Concel.click()

            time.sleep(2)

            Yes = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
            Yes.click()

            try:

                time.sleep(1)

                Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(2)

                print('[{}] User Promotions Concel successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] User Promotions Concel false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Create_Deposit()

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        print('[{}] Approve Deposit Bill Number !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Approve2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div/button')
        Approve2.click()

        Date = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H%M%p")))
        # Time.send_keys('121212')

        time.sleep(2)

        upload = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[5]/div[2]/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\koko.jpg')

        time.sleep(2)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบอนุมัติทันที')

        time.sleep(2)

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

        Cancel_Promotions()

        Create_Deposit()

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        upload = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[2]/div/div/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\momo.jpg')

        print('[{}] Click Approve Upload Slip !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Upload Slip successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Upload Slip false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit_popup = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[3]/div')
        Deposit_popup.click()

        print('[{}] Adjust/Expense !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Adjust_Expense = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[1]/div/div/div[2]/button[2]')
        browser.execute_script("arguments[0].click();", Adjust_Expense)

        time.sleep(2)

        Date = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[1]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[1]/div[4]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H%M%p")))
        # Time.send_keys('121212')

        Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[2]/div[2]/input')
        Amount.send_keys(100)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[2]/div[4]/input')
        Note.send_keys('บอททดสอบสร้างบิลโน๊ต')

        # Upload_Slip = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[3]/div[2]/input')
        # Upload_Slip.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\jojo.jpg')

        time.sleep(2)

        credits = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[4]/div/button')
        browser.execute_script("arguments[0].click();", credits)

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            Adjust_Expense_Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[1]/div/div/div[2]/button[2]')
            browser.execute_script("arguments[0].click();", Adjust_Expense_Close)

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Adjust/Expense successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Adjust/Expense false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Cancel_Promotions()

        Create_Deposit()

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        Cash_System.click()

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        click_Bill_Number = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[1]/div[1]').text

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div/div')
        browser.execute_script("arguments[0].click();", Deposit_popup)


        Search_Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[2]/div[2]/input')
        Search_Amount.send_keys('100')

        click_search = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[3]/div[4]/button')
        click_search.click()

        Bill_Match = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[7]/ul/li[1]')
        Bill_Match.click()

        print('[{}] Click Bill_Match !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Bill_Number = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/input[1]')
        Bill_Number.send_keys(click_Bill_Number)

        upload = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[7]/div/form/div/input[2]')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\popo.jpg')

        Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/input[3]')
        Remark.send_keys('บอททดสอบผูกบิล')

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/div/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/button[1]')
            Close.click()

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            Close.click()

            print('[{}] Bill Number successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Bill Number false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Cancel_Promotions()

        ########## เข้าเว็บหน้าบ้าน ###########

        # browser.get('https://zabtech.xyz/')
        #
        # time.sleep(3)
        #
        # login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()
        #
        # print('[{}] login password !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # username = browser.find_element(By.ID, 'login-phone')
        # username.send_keys(telephone_number)
        #
        # password = browser.find_element(By.ID, 'login-password')
        # password.send_keys(pass_word)
        #
        # try:
        #
        #     password.submit()
        #
        #     time.sleep(3)
        #
        #     profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()
        #
        #     time.sleep(3)
        #
        #     profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()
        #
        #     print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # except:
        #
        #     print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # time.sleep(3)
        #
        # print('[{}] User create deposit promotion !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # ########## รับโปรโมชั่นผ่านลิ้งค์ ###########
        #
        # browser.get('https://zabtech.xyz/promotion/promotion-Tl5YuafCJW')
        #
        # promotion = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/div[3]/button').click()
        #
        # time.sleep(3)
        #
        # try:
        #
        #     time.sleep(3)
        #
        #     money = browser.find_element(By.ID, 'deposit-amount')
        #     money.send_keys('100')
        #     money.submit()
        #
        #     time.sleep(5)
        #
        #     print('[{}] User create deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # except:
        #     print('[{}] User create deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # browser.get('https://s-u-p.zabtech.xyz/')
        #
        # ############# เปลี่ยนธนาคาร ###############
        #
        # time.sleep(2)
        #
        # Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        # Cash_System.click()
        #
        # time.sleep(2)
        #
        # print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        # browser.execute_script("arguments[0].click();", Deposit)
        #
        # time.sleep(2)
        #
        # Change_bank_Account = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[5]/div[3]/span/a')
        # browser.execute_script("arguments[0].click();", Change_bank_Account)
        #
        # print('[{}] click Change bank Account !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # try:
        #     Deposit_Account_Number1 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div[2]/div/button[1]').click()
        #     Deposit_Account_Number2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div[2]/div/ul/li[4]').click()
        #
        #     Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[2]/div[2]/input')
        #     Remark.send_keys('ทดสอบเปลี่ยนบัญชีโดยที่ยังไม่กดอนุมัติ')
        #
        #     click_Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        #     browser.execute_script("arguments[0].click();", click_Save)
        #
        #     time.sleep(2)
        #
        #     Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
        #     Close.click()
        #
        #     print('[{}] Change bank Account successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #
        # except:
        #     print('[{}] Change bank Account false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(10)

        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
