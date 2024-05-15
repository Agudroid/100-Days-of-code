import pandas as pd
import datetime as dt
import random
import smtplib


CONNECTION = "smtp.gmail.com"
EMAIL_ACCOUNT = "aguchu2000m@gmail.com"


def check_birthday(df: pd.DataFrame):
    today = dt.datetime.now()
    for (index, row) in df.iterrows():
        if row.month == today.month and row.day == today.day:
            return row
    return None


def load_df():
    df = pd.read_csv('birthdays.csv')
    return df


def create_letter(person: pd.DataFrame):
    random_number = random.randint(1 ,3)
    with open(f"letter_templates/letter_{random_number}.txt", mode='r') as file:
        letter = file.read()
    letter = letter.replace("[NAME]", person['name'])
    return letter


def send_letter(person, message, subject='Happy Birthday!!'):
    connection = smtplib.SMTP(CONNECTION)
    connection.starttls()
    connection.login(user=EMAIL_ACCOUNT, password="iatz yfix uljd emem")
    connection.sendmail(from_addr=EMAIL_ACCOUNT,
                        to_addrs=person['email'],
                        msg=f"Subject:{subject}\n\n"
                            f"{message}")
    connection.close()


if __name__ == '__main__':
    birthday_df = load_df()
    birthday_person = check_birthday(birthday_df)
    if birthday_person is not None:
        birthday_letter = create_letter(birthday_person)
        send_letter(birthday_person, birthday_letter)




