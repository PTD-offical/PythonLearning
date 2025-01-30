import requests

TodoData = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(TodoData.json())