from bs4 import BeautifulSoup
import requests
con = input("text : ")
URL = 'https://en.wikipedia.org/wiki/' + con
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')

results = soup.find('div', id='mw-content-text').find('div', class_="mw-parser-output").find_all('p', limit=5)
for result in results:
    print(result.get_text().rstrip())