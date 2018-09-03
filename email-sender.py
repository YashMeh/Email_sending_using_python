import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
with open('email.csv','r') as csv_file:
    emails=[]

    for i in csv_file:
        emails.append(i)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("<email>","<password>")
for i in emails:
    msg=MIMEMultipart()
    msg['From']="ym1962956@gmail.com"
    msg['To']=i
    msg['Subject']="Subject"
    msg.attach(MIMEText("Text to be displayed as message", 'plain'))
    server.send_message(msg)
    del msg


