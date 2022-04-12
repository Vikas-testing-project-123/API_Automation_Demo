import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("testtt211999@gmail.com", "Vikash@1999")#you need to change the security settings to login in
server.sendmail("testtt211999@gmail.com",
                "Vikas@kockpit.in",
                "C:\Users\TA0134\PycharmProjects\API_Testing/Report.html")

server.quit()
print("Done")