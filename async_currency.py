# async_currency.py
import asyncio
import aiohttp
import os
import certifi
import ssl

async def get_exchange_rate(session, api_key, base_currency, target_currency="RUB"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        async with session.get(url, ssl=ssl.create_default_context(cafile=certifi.where())) as response:
            data = await response.json()
            if data["result"] == "success":
                rate = data["conversion_rates"][target_currency]
                print(f"1 {base_currency} = {rate} {target_currency}")
                return rate
            else:
                print(f"Ошибка: не удалось получить данные для {base_currency}!")
    except Exception as e:
        print(f"Ошибка сети для {base_currency}: {e}")

async def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Ошибка: задайте API_KEY в переменной окружения!")
        return
    async with aiohttp.ClientSession() as session:
        tasks = [
            get_exchange_rate(session, api_key, "USD"),
            get_exchange_rate(session, api_key, "EUR")
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())