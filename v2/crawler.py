import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# selenium format
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

fill_stop = 0.4
new_page_stop = 4

def register(driver, first_name, last_name, email_address, user_id, password):
# def register(user_id, password, email, first_name, last_name, driver):
    
    driver.get('https://account.teracloud.jp/RegistForm.php/index/')
    # driver.maximize_window()
    actionChains = ActionChains(driver)
    time.sleep(new_page_stop)

    # register page

    checkbox1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[1]/label') # agree
    actionChains.move_to_element(checkbox1).perform()
    checkbox1.click()
    time.sleep(fill_stop)


    checkbox2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[2]/label') # agree
    actionChains.move_to_element(checkbox2).perform()
    checkbox2.click()
    time.sleep(fill_stop)


    checkbox3 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[7]/div[3]/label') # agree
    actionChains.move_to_element(checkbox3).perform()
    checkbox3.click()
    time.sleep(fill_stop)

    First_name = driver.find_element(By.NAME, 'fname')# first name
    actionChains.move_to_element(First_name).perform()
    time.sleep(fill_stop)
    actionChains.click(First_name).perform()
    not_typing(First_name, first_name)


    Last_name = driver.find_element(By.NAME, 'lname')# last name
    actionChains.move_to_element(Last_name).perform()
    time.sleep(fill_stop)
    actionChains.click(Last_name).perform()
    not_typing(Last_name, last_name)


    Mail_address = driver.find_element(By.NAME, 'mailaddress') # email
    actionChains.move_to_element(Mail_address).perform()
    time.sleep(fill_stop)
    actionChains.click(Mail_address).perform()
    not_typing(Mail_address, email_address)


    User_ID = driver.find_element(By.NAME, 'userid') # userid
    actionChains.move_to_element(User_ID).perform()
    time.sleep(fill_stop)
    actionChains.click(User_ID).perform()
    not_typing(User_ID, user_id)


    Password = driver.find_element(By.NAME, 'password1') # password1
    time.sleep(fill_stop)
    actionChains.move_to_element(Password).perform()
    actionChains.click(Password).perform()
    not_typing(Password, password)


    Password_confirmation = driver.find_element(By.NAME, 'password2') # password2
    time.sleep(fill_stop)
    actionChains.move_to_element(Password_confirmation).perform()
    actionChains.click(Password_confirmation).perform()
    not_typing(Password_confirmation, password)
    
    try:
        cloud_flare = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input') # cloud flare check box
        time.sleep(fill_stop)
        actionChains.move_to_element(cloud_flare).perform()
        # actionChains.click(cloud_flare).perform()
        cloud_flare.click()
    except:
        pass

    time.sleep(fill_stop)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[9]/input').click() # next
    next_div = driver.find_element(By.CLASS_NAME, 'registform_submit') # div
    next_div.find_element(By.CLASS_NAME, 'btn').click() # next
    print('send register info')
    time.sleep(fill_stop)

def authentication(driver, verification_code):
    actionChains = ActionChains(driver)
    Verification_Code = driver.find_element(By.NAME, 'authcode')# Verification Code
    actionChains.move_to_element(Verification_Code).perform()
    time.sleep(fill_stop)
    actionChains.click(Verification_Code).perform()
    not_typing(Verification_Code, verification_code)

    time.sleep(fill_stop)
    next_div = driver.find_element(By.CLASS_NAME, 'registform_submit') # div
    next_div.find_element(By.CLASS_NAME, 'btn').click() # next
    print('send Verification Code')
    time.sleep(new_page_stop)


def login(driver, user_id, password, referral_code):
    actionChains = ActionChains(driver)
    driver.get('https://infini-cloud.net/en/modules/mypage/usage/')
    time.sleep(new_page_stop)

    # usage page
    login_button = driver.find_element("xpath", '//*[@id="main"]/div/div/div/a')
    login_button.click() # go to login page
    time.sleep(new_page_stop)

    # login page
    User_ID = driver.find_element(By.CLASS_NAME, 'form-id')
    actionChains.move_to_element(User_ID).perform()
    time.sleep(fill_stop)
    actionChains.click(User_ID).perform()
    not_typing(User_ID, user_id)

    Password = driver.find_element(By.CLASS_NAME, 'form-pw')
    actionChains.move_to_element(Password).perform()
    time.sleep(fill_stop)
    actionChains.click(Password).perform()
    not_typing(Password, password)

    time.sleep(fill_stop)
    driver.find_element(By.ID, 'loginbtn').click() # login
    time.sleep(new_page_stop)

    # MyPage
    driver.find_element(By.NAME, 'introducers_code').send_keys(referral_code) # fill referral code
    time.sleep(fill_stop)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[7]/table/tbody/tr[2]/td/span/span/form/input[2]').click() # apply referral code
    print("flow succeed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    time.sleep(new_page_stop*1.5)


def not_typing(element, text):
    element.send_keys(text)
