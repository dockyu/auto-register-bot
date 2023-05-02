from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks5://localhost:9050')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://icanhazip.com')