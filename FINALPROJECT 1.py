import requests
import time

class CryptoFetcher:
    
    def get_bitcoin_price(self):

        print("...[Fetcher]: Роблю запит до API...")
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()
            return data['bitcoin']['usd']
        except Exception as e:
            print(f"Помилка в Fetcher: {e}")
            return None

class ConsolePrinter:

    def show_price(self, price):
        """
        Дуже простий метод, який
        просто показує ціну.
        """
        if price is not None:
            print(f"\n--- [Printer]: Ваш результат ---")
            print(f"   Поточна ціна Bitcoin: $ {price:,.2f}")
            print(f"---------------------------------")
        else:
            print("\n--- [Printer]: Не вдалося показати ціну ---")


def run():

    print("[RUN]: Програма стартувала.")

    fetcher = CryptoFetcher()
    printer = ConsolePrinter()

    current_price = fetcher.get_bitcoin_price()
    
    printer.show_price(current_price)
    
    print("[RUN]: Програма завершила роботу.")

if __name__ == "__main__":
    run()