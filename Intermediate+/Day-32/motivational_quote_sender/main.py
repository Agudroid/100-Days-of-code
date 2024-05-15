import datetime as dt
from random import choice
import smtplib


CONNECTION = "smtp.gmail.com"
EMAIL_ACCOUNT = "aguchu2000m@gmail.com"
PASSWORD = "iatz yfix uljd emem"


def create_quote_list():
    temporal_quote_list = []
    with open("quotes.txt", mode='r') as file:
        for line in file.readlines():
            temporal_quote_list.append(line)
    return temporal_quote_list


def get_random_quote(quotes):
    return choice(quotes)


def is_monday():
    return dt.datetime.now().weekday() == 0


def send_mail(subject, message):
    connection = smtplib.SMTP(CONNECTION)
    connection.starttls()
    connection.login(user=EMAIL_ACCOUNT, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL_ACCOUNT,
                        to_addrs="agudo.antonio@outlook.com",
                        msg=f"Subject:{subject}\n\n"
                            f"{message}")
    connection.close()


quote_list = create_quote_list()
if not is_monday():
    quote = get_random_quote(quote_list)
    send_mail("Motivation quote", quote)
