from bs4 import BeautifulSoup
import requests
text = input("text : ")
params = {"q": text}
content = requests.get("https://www.bing.com/search", params=params)
soup = BeautifulSoup(content.text, 'html.parser')
results = soup.find('div', id='b_content').find('main').find('ol', id="b_results").find('li', class_="b_ans b_top b_topborder").find('div', class_="dcont dcsbx")

print(results)