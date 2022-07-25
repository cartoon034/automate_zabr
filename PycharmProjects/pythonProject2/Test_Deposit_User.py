from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    #รหัสผ่านแอดมิน
    usernameadmin    = ('admin000033')
    passwordadmin    = ('pp100200')

    #รหัสผ่านผู้ใช้
    telephone_number = ('0825169264')
    pass_word        = ('pp100200')

    #ใส่จำนวนเงิน
    user_keys_money  = (100)

    def login_admin():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(2)

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.NAME, 'username')
        username.send_keys(usernameadmin)

        password = browser.find_element(By.NAME, 'password')
        password.send_keys(passwordadmin)

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def logout_admin():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        print('[{}] logout user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        profileadmin = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button')
        profileadmin.click()

        logoutadmin = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/ul/a[2]')
        logoutadmin.click()

        try:
            username = browser.find_element(By.NAME, 'username')
            username.send_keys('admin000033')

            print('[{}] logout user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] logout user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def login_user():

        time.sleep(1)

        browser.get('https://zabtech.xyz/')

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys(telephone_number)

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys(pass_word)

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def logout_user():

        time.sleep(3)

        profile1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

        time.sleep(1)

        logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        try:

            click_login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

            print('[{}] logout user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] logout user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def User_create_deposit():

        time.sleep(3)

        print('[{}] User create deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/button/span').click()

        time.sleep(3)

        NoPro = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/button[2]').click()

        money = browser.find_element(By.ID, 'deposit-amount')
        money.send_keys(user_keys_money)
        money.submit()

        try:

            time.sleep(3)

            deposit_copy_bank = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/div/div[4]/button').click()

            time.sleep(5)

            print('[{}] User create deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] User create deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def Approve_Deposit_Bill_Numbe():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        print('[{}] Approve Deposit Bill Number !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Approve2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div/button')
        Approve2.click()

        Date = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H%M%p")))
        # Time.send_keys('121212')

        time.sleep(2)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[5]/div[2]/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\koko.jpg')

        time.sleep(2)

        Note = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
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

    def Approve_Deposit_Upload_Slip():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[2]/div/div/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\momo.jpg')

        print('[{}] Click Approve Upload Slip !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Upload Slip successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Upload Slip false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def Adjust_Expense():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

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
        Amount.send_keys(user_keys_money )

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[2]/div[4]/input')
        Note.send_keys('บอททดสอบสร้างบิลโน๊ต')

        Upload_Slip = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[3]/div[2]/input')
        Upload_Slip.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\jojo.jpg')

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

    def Bill_Match():

        time.sleep(1)

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        Cash_System.click()

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        click_Bill_Number = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[1]/div[1]').text

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div/div')
        browser.execute_script("arguments[0].click();", Deposit_popup)

        Search_Amount = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[2]/div[2]/input')
        Search_Amount.send_keys(user_keys_money)

        click_search = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[3]/div[4]/button')
        click_search.click()

        Bill_Match = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[7]/ul/li[1]')
        Bill_Match.click()

        print('[{}] Click Bill Match !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Bill_Number = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/input[1]')
        Bill_Number.send_keys(click_Bill_Number)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[7]/div/form/div/input[2]')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\popo.jpg')

        Remark = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/input[3]')
        Remark.send_keys('บอททดสอบผูกบิล')

        Save = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr/td[7]/div/form/div/div/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/button[1]')
            Close.click()

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            Close.click()

            print('[{}] Bill Match successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Bill Match false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    try:

        login_user()

        User_create_deposit()

        login_admin()





    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)