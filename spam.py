from datetime import datetime
from send_email import *

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

while True:
    if int(now.strftime("%H")) == 10:
        receiver_email = "pierresalama115@gmail.com"
        subject = "WAKE UP!!"
        body = "ITS 9 AM GO CODE MORE COOL STUFF"
        for i in range(0,100):
            sendemail(receiver_email,subject,body)

