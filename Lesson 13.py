import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.content)
print(f"Datatype {type(response.content)}")