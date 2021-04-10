import smtplib
myaddress = "aom_bnn@hotmail.com"
recaddress ="reminder+swiley@swiley.net"
from email.message import EmailMessage
msg = EmailMessage()
msg.set_content("Get ready to pick up Rose!!")
msg['Subject'] = "Reminder"
msg['From'] = myaddress
msg['to'] = recaddress

s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls()
print("enter password for ", myaddress)
s.login(myaddress,input())
s.send_message(msg)
s.quit()
print("done")
