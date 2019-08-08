from bs4 import BeautifulSoup
import requests


text = input("text : ")
text.replace(" ", "+")
params = {"q": text}
content = requests.get("https://duckduckgo.com/?q=", params=params)
soup = BeautifulSoup(content.text, 'html.parser')
res = soup.find_all('div', class_="result__snippet js-result-snippet")
for r in res:
	print(r)
