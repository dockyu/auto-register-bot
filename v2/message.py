import json
import time
from threading import Thread
import threading
import multiprocessing

lock = threading.Lock()
semaphore = threading.Semaphore(2)

class Listen:
    listen = False
    message_ids = []
    email_content = ''

    def message_list(self):
        # lock.acquire()
        url = "https://api.mail.tm/messages"
        headers = { 'Authorization': 'Bearer ' + self.token }
        lock.acquire()
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        time.sleep(1)
        lock.release()
        
        data = response.json()
        return  [
                    msg for i, msg in enumerate(data['hydra:member']) 
                        if data['hydra:member'][i]['id'] not in self.message_ids
                ]

    def message(self, idx):
        url = "https://api.mail.tm/messages/" + idx
        headers = { 'Authorization': 'Bearer ' + self.token }
        lock.acquire()
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        time.sleep(1)
        lock.release()
        return response.json()

    def run(self):
        print('run function')
        while self.listen:
            print('listening')
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message = self.message(message['id'])
                self.listener(message)

            time.sleep(self.interval)

    def receive_one_mail(self):
        print('receive_one_mail function')
        while self.listen:
            # lock.acquire()
            semaphore.acquire()
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message = self.message(message['id'])
                self.listener(message)
                if (message['text']):
                    self.email_content = message['text']
                    # lock.release()
                    return
            semaphore.release()
            # lock.release()
            time.sleep(self.interval)

    def start(self, listener, interval=3):
        if self.listen:
            self.stop()

        self.listener = listener
        self.interval = interval
        self.listen = True

        # Start listening thread
        # self.thread = Thread(target=self.run)
        self.thread = Thread(target=self.receive_one_mail)
        self.thread.start()
    
    def stop_when_finish(self):
        # self.listen = False
        self.thread.join(timeout=60)
        self.listen = False
    
    def stop_force(self):
        self.listen = False
        self.thread.join()

    def get_email_content(self):
        return self.email_content