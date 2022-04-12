import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "testtt211999@gmail.com"
email_send = "Vikas@kockpit.in"

subject = "Response1"
# recepent_list = ["Vikas@kockpit.in", "99singh.vikash@gmail.com"]

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = "Hi, here is teh report of the API test"
msg.attach(MIMEText(body, 'plain'))

filename = 'report.html'
attachment = open(filename,'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('content-Disposition',"attachment; filename="+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_user, "Vikash@1999")#you need to change the security settings to login in
server.sendmail(email_user, email_send, text)

server.quit()
print("Done")
