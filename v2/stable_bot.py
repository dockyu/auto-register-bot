from threading import Thread
import email_module
import crawler
import undetected_chromedriver as uc
import time
import names # generate random name

def listener(message):
        # print("\nSubject: " + message['subject'])
        # print("Content: " + message['text'] if message['text'] else message['html'])
        print("execute listener, get email message")
        # print(message['text'])


def flow(chromedriver_index):
    options = uc.ChromeOptions()
    # PROXY = "103.37.88.10:80"
    # options.add_argument('--proxy-server=%s' % PROXY)
    driver_path = 'D:\\Project\\auto-register-bot\\driver\\chromedriver'+ str(chromedriver_index) +'.exe'
    driver = uc.Chrome(options=options, driver_executable_path=driver_path) 
    # driver.maximize_window() 
    # driver.minimize_window()
    driver.set_window_size(300, 500)
    
    driver.set_window_position(1700, 200)

    try:
         
        # Get Domains
        mail_service = email_module.Email()
        print("\nDomain: " + mail_service.domain)

        # Make new email address
        mail_service.register()
        print("\nEmail Adress: " + str(mail_service.address))

        # temp user information
        tmp_first_name = names.get_first_name()
        tmp_last_name = names.get_last_name()
        tmp_email_address = str(mail_service.address)
        tmp_user_id = tmp_email_address.split('@')[0]
        tmp_password = names.get_full_name()
        my_referral_code = '4S4FP'


        # Start listening one mail
        mail_service.one_bot_start(listener, interval=3)

        # time.sleep(100000)

        # register temp user
        crawler.register(driver, tmp_first_name, tmp_last_name, tmp_email_address, tmp_user_id, tmp_password)

        # Stop listening when get email
        mail_service.stop_when_finish()

        tmp_verification_code = None
        mail_content = mail_service.get_email_content()
        for line in mail_content.splitlines():
            if 'Verification Code' in line: # find line with verification code
                tmp_verification_code = line.split(": ")[1]
        
        if tmp_verification_code == None:
            print("Verification Code not found.")
            driver.close()
            return

        print("Verification Code : " + tmp_verification_code)

        # authenticate email
        crawler.authentication(driver, tmp_verification_code)

        crawler.login(driver, tmp_user_id, tmp_password, my_referral_code)
    except Exception as e:
        print(e)
        mail_service.stop_force()
        driver.close()
        return

    driver.close()





if __name__ == "__main__":
     
     while True:
        for i in range(6):
            flow(0)
            time.sleep(1)
        time.sleep(300)
    # 創建5個thread
    # threads = []
    # for i in range(1):
    #     t = Thread(target=flow, args=(i,))
    #     threads.append(t)

    # # 啟動所有thread
    # for t in threads:
    #     t.start()
    
    # # 等待所有thread結束
    # for i in range(len(threads)):
    #     if i==0:
    #         threads[i].join(timeout=60)
    #     elif i==1:
    #         threads[i].join(timeout=30)
    #     else:
    #         threads[i].join(timeout=1)
    


    
