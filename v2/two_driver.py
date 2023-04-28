from threading import Thread
from selenium import webdriver
import time

def test():
    print('test')
    a = webdriver.Chrome()
    a.get('https://www.baidu.com')
    time.sleep(10)
    a.quit()

if __name__ == "__main__":
    # 創建5個thread
    threads = []
    for i in range(2):
        t = Thread(target=test)
        threads.append(t)

    # 啟動所有thread
    for t in threads:
        t.start()
    
    # 等待所有thread結束
    for i in range(len(threads)):
        if i==0:
            threads[i].join(timeout=60)
        elif i==1:
            threads[i].join(timeout=30)
        else:
            threads[i].join(timeout=1)