import requests as req

response = req.get('https://jsonplaceholder.typicode.com/posts/1')

print(response.status_code)

print(response.json())