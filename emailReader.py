import poplib, email, string,re, pygame, time

running = False

t_end = time.time() + 60 * 10

while time.time() < t_end:
    mailserver = poplib.POP3_SSL('pop.gmail.com')
    mailserver.user('recent:')  # use 'recent mode' email address
    mailserver.pass_('')  # consider not storing in plaintext!
    numMessages = len(mailserver.list()[1])
    msg = mailserver.retr(numMessages)
    str = string.join(msg[1], "\n")
    mail = email.message_from_string(str)

    yesAlarm = '<html><head><metahttp-equiv="Content-Type"content="text/html;charset=UTF-8"/><title>MultimediaMessage</title></head><bodyleftmargin="0"topmargin="0"><trheight="15"style="border-top:1pxsolid#0F7BBC;"><td>1</td></tr></body></html>'
    noAlarm = '<html><head><metahttp-equiv="Content-Type"content="text/html;charset=UTF-8"/><title>MultimediaMessage</title></head><bodyleftmargin="0"topmargin="0"><trheight="15"style="border-top:1pxsolid#0F7BBC;"><td>2</td></tr></body></html>'

    for part in mail.walk():
        body = part.get_payload()

    #body = mail.get_payload()[0]#.get_payload()
    body = re.sub('[\s+]','',body)

    if body == yesAlarm and running == False :
	running = True
        print ("Alarm on")
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.wav")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
	    continue
    elif body == noAlarm and running == True:
        running = False
        print ("Alarm off")
        mailserver.dele(numMessages)
    else:
        pass

