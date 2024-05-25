from bs4 import BeautifulSoup
import requests

response = requests.get("https://en.wikipedia.org/wiki/Cat_(Unix)")

if response.status_code == 200:
    soup = BeautifulSoup(response.text,features="html.parser")
    soup_list = soup.find_all('and')
    for value in soup_list:
        all_td = value.find_all('td')
        print(all_td[3].find('code').text)