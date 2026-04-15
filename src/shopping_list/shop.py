import sys
from storage import load_list, save_list

def main():
    if len(sys.argv) < 2:
        print("Kļūda: Nav norādīta komanda (add, list, total, clear)")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Lūdzu norādiet produktu un cenu! Piemērs: python3 shop.py add Maize 1.20")
            return
            
        name = sys.argv[2]
        try:
            price = float(sys.argv[3])
        except ValueError:
            print("Kļūda: Cenai jābūt skaitlim!")
            return
        
        items = load_list()
        items.append({"name": name, "price": price})
        save_list(items)
        print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

    elif command == "list":
        items = load_list()
        if not items:
            print("Saraksts ir tukšs.")
            return
            
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item['name']} — {item['price']:.2f} EUR")

    elif command == "total":
        items = load_list()
        total = sum(item['price'] for item in items)
        print(f"Kopā: {total:.2f} EUR ({len(items)} produkti)")

    elif command == "clear":
        save_list([])
        print("✓ Saraksts notīrīts.")

    else:
        print(f"Nezināma komanda: {command}")

if __name__ == "__main__":
    main()
    