from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')
headers = soup.find_all('h2')
print(headers)
print(headers[0].text, end="\n\n")

intro = soup.find_all('div', {'class': 'introduction'})
print(intro)
print(intro[0].text)
