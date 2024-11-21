from bs4 import BeautifulSoup

html = "<html><body><p>Hello, World!</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.p.text)
