import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/dp/B08N5VSQNG/ref=fs_a_mn_2'

headers = {
    "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
           }
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:13].replace(',', ''))



    print(converted_price)
    print(title.strip())

    if (converted_price < 150000):
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('<enter your mail>', '<enter your password>')

    subject = 'Price fell down!'
    body = 'Check amazon link https://www.amazon.in/dp/B08N5VSQNG/ref=fs_a_mn_2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender mail',
        'reciever mail',
        msg
    )

    print('Hey email has been sent!')
    server.quit()

check_price()
