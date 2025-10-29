import requests
import locale
from datetime import datetime

try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    print("Локаль en_US.UTF-8 не знайдена, використовується стандартна.")


class CryptoDataFetcher:

    def fetch_fear_and_greed_index(self):

        try:
            response = requests.get("https://api.alternative.me/fng/?limit=1")
            response.raise_for_status()
            
            data = response.json()
            
            if data and 'data' in data and len(data['data']) > 0:
                index_data = data['data'][0]
                value = int(index_data['value'])
                classification = index_data['value_classification']
                return f"{value} - {classification}"
            
        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні індексу F&G: {e}")
        return "Недоступний"

    def fetch_top_10_coins(self):

        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': 'false'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні даних з CoinGecko: {e}")
        return None


class MarketAnalyzer:

    def find_market_movers(self, coins_data):

        if not coins_data:
            return None, None, None

        try:
            biggest_gainer = max(coins_data, key=lambda x: x.get('price_change_percentage_24h', 0))
            
            biggest_loser = min(coins_data, key=lambda x: x.get('price_change_percentage_24h', 0))
            
            highest_volume = max(coins_data, key=lambda x: x.get('total_volume', 0))
            
            return biggest_gainer, biggest_loser, highest_volume
        
        except Exception as e:
            print(f"Помилка під час аналізу даних: {e}")
            return None, None, None


class ConsoleReporter:

    def _format_currency(self, value):
        return locale.format_string("%d", value, grouping=True)

    def print_report(self, fng_index, gainer, loser, volume_leader):

        print("=" * 40)
        print(f" ЗВІТ ПО РИНКУ КРИПТОВАЛЮТ")
        print(f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 40)
        
        print(f"\n Загальний Настрій Ринку (Fear & Greed): {fng_index}\n")
        print("-" * 40)
        
        if gainer:
            print(" ЛІДЕР РОСТУ (24г):")
            print(f"   Монета: {gainer['name']} ({gainer['symbol'].upper()})")
            print(f"   Ціна: ${gainer['current_price']:,.4f}")
            print(f"   Зміна: +{gainer['price_change_percentage_24h']:.2f}%")
            print(f"   Обсяг: ${self._format_currency(gainer['total_volume'])}")
            print("-" * 40)

        if loser:
            print(" ЛІДЕР ПАДІННЯ (24г):")
            print(f"   Монета: {loser['name']} ({loser['symbol'].upper()})")
            print(f"   Ціна: ${loser['current_price']:,.4f}")
            print(f"   Зміна: {loser['price_change_percentage_24h']:.2f}%")
            print(f"   Обсяг: ${self._format_currency(loser['total_volume'])}")
            print("-" * 40)

        if volume_leader:
            print(" ЛІДЕР ЗА ОБСЯГОМ ТОРГІВ (24г):")
            print(f"   Монета: {volume_leader['name']} ({volume_leader['symbol'].upper()})")
            print(f"   Обсяг: ${self._format_currency(volume_leader['total_volume'])}")
            print(f"   Зміна (24г): {volume_leader['price_change_percentage_24h']:.2f}%")
            print("=" * 40)


def run():

    print("Запуск програми...")
    
    fetcher = CryptoDataFetcher()
    analyzer = MarketAnalyzer()
    reporter = ConsoleReporter()
    
    print("Отримання даних з API...")
    fng_index = fetcher.fetch_fear_and_greed_index()
    coins_data = fetcher.fetch_top_10_coins()
    
    if not coins_data:
        print("Не вдалося отримати дані по монетах. Завершення роботи.")
        return
        
    print("Аналіз даних...")
    gainer, loser, volume_leader = analyzer.find_market_movers(coins_data)
    
    print("Формування звіту...")
    reporter.print_report(fng_index, gainer, loser, volume_leader)

if __name__ == "__main__":
    run()