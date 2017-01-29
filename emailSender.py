#!/usr/bin/python

import smtplib, sys, os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

imageName = str(sys.argv[1])
email = "" #set email
password = "" # set password
receiver = "7075085101@mms.att.net"
text = """View Camera at http://bpnguyen.com. REPLY "1" to sound alarm or "2" to turn off alarm""" #create message
subject = "There has been a motion!"

def sendMail(imageName):
    imageData = open(imageName, 'rb').read()
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = "Security System"
    message['To'] = receiver

    body = MIMEText(text)
    message.attach(body)
    image = MIMEImage(imageData, name=os.path.basename(imageName))
    message.attach(image)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587) #find your mail server using google.com, we use gmail as an example. change for yahoo mail, outlook, etc
    mailServer.ehlo()
    mailServer.starttls() #this enables encryption
    mailServer.ehlo()
    mailServer.login(email, password) #username and password login

    mailServer.sendmail(email, receiver, message.as_string()) #send it
    mailServer.quit()

receivers = ["7075085101@mms.att.net"]
	
sendMail(imageName)
