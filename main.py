import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 300

product_URL = "https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07L5GDTYY/ref=sr_1_8?dchild=1&keywords=kindle&qid=1633235917&s=amazon-devices&sr=1-8"
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
     "Accept-Language":"en-us"
}

response =requests.get(product_URL, headers=header)

soup = BeautifulSoup(response.content,"lxml")

price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("testttest030@gmail.com", "qpwo1029")
        connection.sendmail(
            from_addr="testttest030@gmail.com",
            to_addrs="testttest030@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_URL}"
        )
