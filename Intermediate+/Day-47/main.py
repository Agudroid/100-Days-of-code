from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

URL_PAGE = os.getenv("URL_PAGE")
DESTINATION_MAIL = os.getenv("DESTINATION_MAIL")
SOURCE_MAIL = os.getenv("SOURCE_MAIL")
GMAIL_CONNECTION = os.getenv("GMAIL_CONNECTION")
APPLICATION_PASSWORD = os.getenv("APPLICATION_PASSWORD")


def find_price(url:str)-> float:
    print(f"url page: {URL_PAGE}")

    response = requests.get(url, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept-Language' : 'en-US,en;q=0.9'
        }
    )
    html_page = BeautifulSoup(response.content, 'html.parser')
    print(html_page.prettify())
    price_string = html_page.find(class_="a-offscreen").get_text()
    price_float = float(price_string[1:])
    return price_float

def send_mail(email:str, price:float):
    connection = smtplib.SMTP(GMAIL_CONNECTION, port=587)
    connection.starttls()
    connection.login(user=SOURCE_MAIL, password=APPLICATION_PASSWORD)
    connection.sendmail(from_addr=SOURCE_MAIL,
                        to_addrs=DESTINATION_MAIL,
                        msg= f"""Subject: Price Alert\n\n
                        Your desire product is now {price}$ check this link to buy it:
                        https://appbrewery.github.io/instant_pot/ 
                        """)
    connection.close()

if __name__ == '__main__':
    price = find_price(URL_PAGE)
    print(f"Product Price: {price}$")
    if price < 100:
        print(f"Sending mail..")
        send_mail(email=DESTINATION_MAIL, price=price)
        print(f"Mail sent")
    