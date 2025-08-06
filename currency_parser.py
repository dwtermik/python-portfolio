# currency_parser.py
import requests
import os

def get_exchange_rate(api_key, base_currency="USD", target_currency="RUB"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            rate = data["conversion_rates"][target_currency]
            print(f"1 {base_currency} = {rate} {target_currency}")
            return rate
        else:
            print("Ошибка: не удалось получить данные!")
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Ошибка: задайте API_KEY в переменной окружения!")
        return
    print("Курс валют (USD к RUB)")
    get_exchange_rate(api_key)

if __name__ == "__main__":
    main()