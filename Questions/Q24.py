import validators

urls = ["https://www.example.com",
"http://invalid-url",
"ftp://ftp.example.com",
"www.example.com",
"example.com"]

for url in urls:
print(f"The URL {url} is", end=" ")
if validators.url(url):
print("Valid")
else:
print("Invalid")
