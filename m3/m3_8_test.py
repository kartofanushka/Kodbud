# import m3_8

import smtplib
MY_EMAIL=''
MY_PASSWORD=''

with smtplib.SMTP('google')as connection:
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(from_addr="",to_addrs="",msg="Hi, How r u",) #?