from lxml import html
import requests

response = requests.get("https://google.com")
tree = html.fromstring(response.content)
links = tree.xpath("//a/@href")
print(f"{len(links)} links found on the page", *links, sep="\n")
