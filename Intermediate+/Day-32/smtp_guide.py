import smtplib
import datetime as dt

# OUTLOOK_CONNECTION = "smtp.gmail.com"
# EMAIL_ACCOUNT = "aguchu2000m@gmail.com"
#
# connection = smtplib.SMTP(OUTLOOK_CONNECTION)
# connection.starttls()
# connection.login(user=EMAIL_ACCOUNT, password="iatz yfix uljd emem")
# connection.sendmail(from_addr=EMAIL_ACCOUNT,
#                     to_addrs="agudo.antonio@outlook.com",
#                     msg="Subject:Happy Birthday\n\n"
#                         "This is the body of my email")
# connection.close()

current_day = dt.datetime.now()
print(current_day.weekday())

date_of_birth = dt.datetime(year=2000, month=7, day=18)
