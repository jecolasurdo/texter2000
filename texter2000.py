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

# append vtext.com for verizon numbers.
# tmobile numbers need tmomail.net appended.
# tmobile tends to block texts from email. Some brief research shows there might
# be a workaround for this, but I haven't tried it out.
# https://support.t-mobile.com/thread/138127
phone_numbers = [
    "1112223333@vtext.com",
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
