import json
import os

FILE_NAME = "shopping.json"
PRICES_FILE = "prices.json"

def load_list():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def load_prices():
    """Nolasa prices.json, atgriež dict. Ja nav — atgriež {}"""
    if not os.path.exists(PRICES_FILE):
        return {}
    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_prices(prices):
    """Saglabā cenu vārdnīcu JSON failā"""
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)

def get_price(name):
    """Atgriež cenu vai None, ja nav"""
    prices = load_prices()
    return prices.get(name) # .get() automātiski atgriež None, ja neatrod vārdu

def set_price(name, price):
    """Saglabā/atjaunina cenu datubāzē"""
    prices = load_prices()
    prices[name] = price
    save_prices(prices)
    
