import email_module



if __name__ == "__main__":
    def listener(message):
        # print("\nSubject: " + message['subject'])
        # print("Content: " + message['text'] if message['text'] else message['html'])
        print("execute listener, get email message")

    # Get Domains
    test = email_module.Email()
    print("\nDomain: " + test.domain)

    # Make new email address
    test.register()
    print("\nEmail Adress: " + str(test.address))

    # Start listening
    test.start(listener)
    print("\nWaiting for new emails...")

    # Stop listening
    test.stop()
    content = test.get_email_content()

    print(content)
