import requests

print("--- Результат Примера 1 ---")
response1 = requests.post("https://httpbin.org/post",
                          data="Test data",
                          headers={"h1": "Test title"})
print(response1.text)


print("\n--- Результат Примера 2 ---")
response2 = requests.post("https://httpbin.org/post",
                          data={"Test data": "value"})
print(response2.text)