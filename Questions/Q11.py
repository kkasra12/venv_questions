import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()
for key, value in data.items():
print(f"{key} is {value}")

