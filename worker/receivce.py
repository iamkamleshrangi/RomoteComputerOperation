import imaplib
import email
import re
import os
from datetime import date, datetime, time, timedelta
from email.utils import parsedate_tz, mktime_tz, formatdate

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "computermailservices" + ORG_EMAIL
FROM_PWD    = "Test@123"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

#login to the account 
def readmail():
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	mail.login(FROM_EMAIL,FROM_PWD)
	mail.select('inbox')
	type, data = mail.search(None, 'ALL')
	mail_ids = data[0]
	id_list = mail_ids.split()
	latest_email_id = int(id_list[-1])

	status, data = mail.fetch(latest_email_id, '(RFC822)' ) 
	if status != 'OK':
        	print "ERROR getting message", latest_email_id
        	return

	msg = email.message_from_string(data[0][1])

	content_type = msg['Content-Type']
        subject = msg['Subject']

	date = msg['Date'].replace('+0530','0000')
	print date
	print '---------------'
	print datetime.strptime( date, '%a, %d %b %Y %H:%M:%S %Z')
	
'''
	if re.match(r'restart', subject):
		print "System goes to reboot"
		os.system('reboot')

	if re.match(r'shutdown',subject):
		print "System goes to shutdown"
		os.system('shutdown')
'''
readmail()
