import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.glassdoor.com/api/api.htm?version=1&action=employer-review&t.s=w-l&t.a=c&format=300x250&employerId=1651")
soup = BeautifulSoup(page.text, "html.parser")
print(soup)