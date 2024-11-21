from bs4 import BeautifulSoup
import requests

response = requests.get("https://google.com")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.string)
