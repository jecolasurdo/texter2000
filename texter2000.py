from random import randrange 
import time
import smtplib

funny_things = [
    "Yuck! Do you smell that???",
    "Hello?!?!?!",
    "Stinky!",
    "Is this anoying???",
    "Is your refrigerator running????"
]

phone_numbers = [
    "2539510932@vtext.com",
    "2532506766@vtext.com",
    "4063964139@tmomail.net",
    "4065440189@tmomail.net",
    "2532022846@vtext.com",
    "4065811317@tmomail.net" #eric
]

def main():
    print("connecting to gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print("logging into gmail...")
    server.login("aaricstexter2000", "PASSWORD")
    while True:
        print("running...")
        for phone_number in phone_numbers:
            print("Texting ", phone_number)
            message = funny_things[randrange(len(funny_things) -1 )]
            server.sendmail("aaricstexter2000@gmail.com",phone_number,message)
            print("success!")
        print("waiting for next run...")
        time.sleep(300)
        

if __name__ == '__main__':
    main()
