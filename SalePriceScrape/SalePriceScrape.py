# requests library handles http request and mozilla headers
import requests
from bs4 import BeautifulSoup

# defining URL and headers and finally HTTP request with defined headers
URL = "https://www.williams-sonoma.com/products/breville-smart-oven-pro-with-light/?pkey=ctoasters-ovens/"
headers = {"User-Agent":"Mozilla/5.0"}
page = requests.get(URL, headers=headers)

# parsing the website with BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# parse parent tree into list
sale_price_container = soup.find_all("span", class_="product-price")

# step through list with for loop
for pricing in sale_price_container:
    suggested_price = pricing.find("span", class_="price-state price-strike-special")
    discounted_price = pricing.find("span", class_="price-state price-special")
    print(suggested_price.prettify())
    print(discounted_price.prettify())

exit()