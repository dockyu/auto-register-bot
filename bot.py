from mailtm import Email
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

# code file path
code_file_path = 'D:\Project\FreeMaster\project\code.txt'

# selenium format
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

def register(user_id, password, email, driver):
    
    driver.get('https://account.teracloud.jp/RegistForm.php/index/')
    driver.maximize_window() 
    actionChains = ActionChains(driver)
    time.sleep(3)

    # register page

    checkbox1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[1]/label') # agree
    actionChains.move_to_element(checkbox1).perform()
    checkbox1.click()
    time.sleep(0.3)


    checkbox2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[2]/label') # agree
    actionChains.move_to_element(checkbox2).perform()
    checkbox2.click()
    time.sleep(0.3)


    checkbox3 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[3]/label') # agree
    actionChains.move_to_element(checkbox3).perform()
    checkbox3.click()
    time.sleep(0.3)

    First_name = driver.find_element(By.NAME, 'fname')# first name
    actionChains.move_to_element(First_name).perform()
    time.sleep(0.3)
    actionChains.click(First_name).perform()
    not_typing(First_name, 'test')


    Last_name = driver.find_element(By.NAME, 'lname')# last name
    actionChains.move_to_element(Last_name).perform()
    time.sleep(0.3)
    actionChains.click(Last_name).perform()
    not_typing(Last_name, 'test')


    Mail_address = driver.find_element(By.NAME, 'mailaddress') # email
    actionChains.move_to_element(Mail_address).perform()
    time.sleep(0.3)
    actionChains.click(Mail_address).perform()
    not_typing(Mail_address, email)


    User_ID = driver.find_element(By.NAME, 'userid') # userid
    actionChains.move_to_element(User_ID).perform()
    time.sleep(0.3)
    actionChains.click(User_ID).perform()
    not_typing(User_ID, user_id)


    Password = driver.find_element(By.NAME, 'password1') # password1
    time.sleep(0.3)
    actionChains.move_to_element(Password).perform()
    actionChains.click(Password).perform()
    not_typing(Password, password)


    Password_confirmation = driver.find_element(By.NAME, 'password2') # password2
    actionChains.move_to_element(Password_confirmation).perform()
    time.sleep(0.3)
    actionChains.click(Password_confirmation).perform()
    not_typing(Password_confirmation, password)
    


    time.sleep(0.3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[9]/input').click() # next
    next_div = driver.find_element(By.CLASS_NAME, 'registform_submit') # div
    next_div.find_element(By.CLASS_NAME, 'btn').click() # next
    print('send register info')

    return driver

def authentication(driver, code):
    actionChains = ActionChains(driver)
    Verification_Code = driver.find_element(By.NAME, 'authcode')# Verification Code
    actionChains.move_to_element(Verification_Code).perform()
    time.sleep(0.3)
    actionChains.click(Verification_Code).perform()
    not_typing(Verification_Code, code)

    time.sleep(3)
    next_div = driver.find_element(By.CLASS_NAME, 'registform_submit') # div
    next_div.find_element(By.CLASS_NAME, 'btn').click() # next
    print('send Verification Code')
    time.sleep(3)

def login(driver, user_id, password, Referral_Code):
    actionChains = ActionChains(driver)
    driver.get('https://infini-cloud.net/en/modules/mypage/usage/')
    time.sleep(3)

    # usage page
    login_button = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/ul/li[1]/a')
    login_button.click() # go to login page
    time.sleep(3)

    # login page
    User_ID = driver.find_element(By.CLASS_NAME, 'form-id')
    actionChains.move_to_element(User_ID).perform()
    time.sleep(0.3)
    actionChains.click(User_ID).perform()
    not_typing(User_ID, user_id)

    Password = driver.find_element(By.CLASS_NAME, 'form-pw')
    actionChains.move_to_element(Password).perform()
    time.sleep(0.3)
    actionChains.click(Password).perform()
    not_typing(Password, password)

    time.sleep(0.4)
    driver.find_element(By.ID, 'loginbtn').click() # login
    time.sleep(3)

    # MyPage
    driver.find_element(By.NAME, 'introducers_code').send_keys(Referral_Code) # fill referral code
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[7]/table/tbody/tr[2]/td/span/span/form/input[2]').click() # apply referral code


    time.sleep(3)


def not_typing(element, text):
    element.send_keys(text)


def listener(message):
    content = message['text']
    for line in content.splitlines():
        if 'Verification Code' in line: # find line with verification code
            # split "Verification Code: f9de1c6f404b95a005cb58656ff4c415"
            code = line.split(": ")[1]
            # write code to file
            with open(code_file_path, 'w') as f:
                f.write(code)
            

    
def flow():

    # delete file code
    if os.path.isfile(code_file_path):
        os.remove(code_file_path)
        print(f"{code_file_path} deleted.")
    else:
        print(f"{code_file_path} not found.")


    # Get Domains
    test = Email()
    print("\nDomain: " + test.domain)

    # Make new email address
    # test.register(username='test9516', password=None, domain='bugfoo.com')
    test.register()
    email_address = str(test.address)
    user_id = email_address.split('@')[0]
    print("\nEmail Adress: " + email_address)
    print("\nUser ID: " + user_id)

    options = uc.ChromeOptions()
    options.add_argument("--window-size=900,700")
    driver = uc.Chrome(use_subprocess=True, options=options) 
    
    # Start listening
    test.start(listener)
    try:
        print("\nWaiting for new emails...")

        # register
        driver = register(user_id, 'testtest', email_address, driver)
        time.sleep(2)

        time.sleep(8)

        # loop 10 times to get code
        code = ''
        for i in range(8):
            time.sleep(2)
            if os.path.isfile(code_file_path):
                with open(code_file_path, 'r') as f:
                    code = f.read()
            if code:
                break

        if not code: # not get code until 24 sec
            print("Failed to get code")
            test.stop()
            return

        print('get code from code.txt: ', code)
        
        # delete file code
        if os.path.isfile(code_file_path):
            os.remove(code_file_path)
            print(f"{code_file_path} deleted.")
        else:
            print(f"{code_file_path} not found.")

    except Exception as e:
        test.stop()
        driver.close()
        return

    test.stop()

    authentication(driver, code)

    login(driver, user_id, 'testtest', '4S4FP')

    time.sleep(3)

    driver.close()



if __name__ == "__main__":
    while True:
        try:
            flow()
        except Exception as e:
            if e == KeyboardInterrupt:
                exit()