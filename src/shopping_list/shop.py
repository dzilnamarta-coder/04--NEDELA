import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units

def main():
    if len(sys.argv) < 2:
        print("Kļūda: Nav norādīta komanda (add, list, total, clear)")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 5:
            print("Lūdzu norādiet produktu, daudzumu un cenu! Piemērs: python3 shop.py add Maize 3 1.20")
            return
            
        name = sys.argv[2]
        
        try:
            qty = int(sys.argv[3])
            price = float(sys.argv[4])
            if qty <= 0 or price <= 0:
                print("Kļūda: Daudzumam un cenai jābūt lielākai par 0!")
                return
        except ValueError:
            print("Kļūda: Daudzumam jābūt veselam skaitlim un cenai jābūt skaitlim!")
            return
        
        items = load_list()
        item = {"name": name, "qty": qty, "price": price}
        items.append(item)
        save_list(items)
        
        total = calc_line_total(item)
        print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {total:.2f} EUR")

    elif command == "list":
        items = load_list()
        if not items:
            print("Saraksts ir tukšs.")
            return
            
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            total = calc_line_total(item)
            print(f"  {i}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {total:.2f} EUR")

    elif command == "total":
        items = load_list()
        grand_total = calc_grand_total(items)
        units = count_units(items)
        products = len(items)
        print(f"Kopā: {grand_total:.2f} EUR ({units} vienības, {products} produkti)")

    elif command == "clear":
        save_list([])
        print("✓ Saraksts notīrīts.")

    else:
        print(f"Nezināma komanda: {command}")

if __name__ == "__main__":
    main()
    