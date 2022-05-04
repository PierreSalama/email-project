from send_email import *
from datetime import datetime

friends_birthday = {
    "07-07": "Mina",
    "10-22": "Marcus" ,
    "05-02": "Pierre"
}

friendsToEmail = {
    "Pierre": "pierresalama115@gmail.com",
    "Mina": "mnpgaming935@gmail.com",
    "Marcus":"sharkteeth55@gmail.com"
}

def send(email):
    receiver_email = email
    subject = "Happy Birthday"
    body = "WoW u getting old XD"

    for i in range(0,1):
        sendemail(receiver_email,subject,body)

while True:
    today = datetime.today().strftime('%m-%d')
    for i in friends_birthday:
        if i == today:
            birthdayboy = friends_birthday[today]
            send(friendsToEmail[birthdayboy])
            
            


