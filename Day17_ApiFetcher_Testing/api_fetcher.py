import requests
import json
import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR,
                    format="%(asctime)s %(levelname)s:%(message)s")

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None

def extract_prices(data, keyword=None):
    # For ExchangeRate API structure
    try:
        rates = data["rates"]
        result = {}
        for code, value in rates.items():
            if (not keyword) or (keyword.lower() in code.lower()):
                result[code] = value
        return result
    except (KeyError, TypeError):
        print("Unexpected JSON structure.")
        return {}

def print_and_save_report(prices, filename="btc_price_report.txt"):
    lines = ["📊 Bitcoin Price Report", "--------------------------"]
    for code, value in prices.items():
        lines.append(f"{code}: {value}")
    report = "\n".join(lines)
    print(report)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    try:
        url = input("Enter API URL (or press Enter for default): ").strip()
        if not url:
            url = "https://api.exchangerate-api.com/v4/latest/USD"
        keyword = input("Enter a keyword to filter currencies (or press Enter to show all): ").strip()
        data = fetch_api_data(url)
        if data:
            prices = extract_prices(data, keyword if keyword else None)
            print_and_save_report(prices)
    except Exception as e:
        print("An error occurred. Check error_log.txt for details.")
        logging.error("Exception occurred", exc_info=True)