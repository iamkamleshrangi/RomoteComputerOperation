# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("computermailservices@gmail.com", "Test@123")
 
# message to be sent
print dir(s.rcpt)

# sending the mail
msg = "\r\n".join([
  "Subject: Hello Amit",
  "",
  "Why, oh why"
  ])

s.sendmail("computermailservices@gmail.com", "amitvits2012@gmail.com", msg)
 
# terminating the session
s.quit()
