import requests
from bs4 import BeautifulSoup

url = "https://bank.gov.ua/ua/markets/exchangerates"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

rate_cell = soup.find('td', string='USD').find_next_sibling('td', {'data-label': 'Офіційний курс'})
rate = float(rate_cell.text.replace(',', '.'))

class Converter:

    def __init__(self, r):
        self.r = r

    def to_usd(self, uah):
        return uah / self.r

print(f"Курс: {rate}")