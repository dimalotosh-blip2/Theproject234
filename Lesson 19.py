user_input = input("Введіть число: ")

try:
    number = int(user_input)
    print(f"Ви ввели ціле число: {number}")

except ValueError:
    print(f"Помилка: '{user_input}' не є цілим числом.")