from selenium import webdriver
from selenium.webdriver.common.by import By
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

def login(id, password, Referral_Code):
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://infini-cloud.net/en/modules/mypage/usage/')
    time.sleep(3)

    # usage page
    login_button = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/ul/li[1]/a')
    login_button.click() # go to login page
    time.sleep(3)

    # login page
    # fill id and password to login
    driver.find_element(By.CLASS_NAME, 'form-id').send_keys(id)
    driver.find_element(By.CLASS_NAME, 'form-pw').send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID, 'loginbtn').click() # login
    time.sleep(3)

    # MyPage
    driver.find_element(By.NAME, 'introducers_code').send_keys(Referral_Code) # fill referral code
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[7]/table/tbody/tr[2]/td/span/span/form/input[2]').click() # apply referral code


    time.sleep(50)

    driver.quit()


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    login('test6test', 'testtest', '4S4FP')