import csv
import requests
from bs4 import BeautifulSoup

# url,req,soup
url = "http://uad.ac.id/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
out = soup.find_all('a')
for link in soup.find_all('a'):
    print(link.get('href'))

file = csv.writer(open("output.csv", "w"))
file.writerow([soup.find_all('a')])
