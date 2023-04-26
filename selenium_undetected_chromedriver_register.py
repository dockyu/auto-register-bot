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

def register(user_id, password, email, option):
    driver = uc.Chrome(use_subprocess=True, options=option) 
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
    typing(First_name, 'test')


    Last_name = driver.find_element(By.NAME, 'lname')# last name
    actionChains.move_to_element(Last_name).perform()
    time.sleep(0.3)
    actionChains.click(Last_name).perform()
    typing(Last_name, 'test')


    Mail_address = driver.find_element(By.NAME, 'mailaddress') # email
    actionChains.move_to_element(Mail_address).perform()
    time.sleep(0.3)
    actionChains.click(Mail_address).perform()
    typing(Mail_address, email)


    User_ID = driver.find_element(By.NAME, 'userid') # userid
    actionChains.move_to_element(User_ID).perform()
    time.sleep(0.3)
    actionChains.click(User_ID).perform()
    typing(User_ID, user_id)


    Password = driver.find_element(By.NAME, 'password1') # password1
    time.sleep(0.3)
    actionChains.move_to_element(Password).perform()
    actionChains.click(Password).perform()
    typing(Password, password)


    Password_confirmation = driver.find_element(By.NAME, 'password2') # password2
    actionChains.move_to_element(Password_confirmation).perform()
    time.sleep(0.3)
    actionChains.click(Password_confirmation).perform()
    typing(Password_confirmation, password)
    


    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/div/div[9]/input').click() # next
    next_div = driver.find_element(By.CLASS_NAME, 'registform_submit') # div
    next_div.find_element(By.CLASS_NAME, 'btn').click() # next
    print('send')


    time.sleep(1000)

    # driver.close()

def typing(element, text):
    # loop for all chat in text
    for i in range(len(text)):
        element.send_keys(text[i])
        time.sleep(0.3)
    time.sleep(1.3)

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_extension('register\extension_1_49_0_0.crx')
    options.add_argument("--window-size=900,700")
    # options.add_argument("--disable-javascript")
    register('test13test', 'testtest', 'test4@gmail.com', options)