import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units

def main():
    if len(sys.argv) < 2:
        print("Kļūda: Nav norādīta komanda (add, list, total, clear)")
        return

    command = sys.argv[1]

    if command == "add":
        # Tagad mums vajag vismaz 4 vārdus (python3 shop.py add Maize 3)
        if len(sys.argv) < 4:
            print("Lūdzu norādiet produktu un daudzumu! Piemērs: python3 shop.py add Maize 3")
            return
            
        name = sys.argv[2]
        
        try:
            qty = int(sys.argv[3])
            if qty <= 0:
                print("Kļūda: Daudzumam jābūt lielākam par 0!")
                return
        except ValueError:
            print("Kļūda: Daudzumam jābūt veselam skaitlim!")
            return

        # --- JAUNĀ CENU LOĢIKA ---
        price = get_price(name)

        if price is not None:
            print(f"Atrasta cena: {price:.2f} EUR/gab.")
            
            while True: # Cikls, kas prasa ievadi, kamēr tā ir derīga
                choice = input("[A]kceptēt / [M]ainīt? > ").strip().lower()
                
                if choice == 'a':
                    break # Cena paliek tāda pati, izejam no cikla
                elif choice == 'm':
                    while True: # Cikls, lai paprasītu pareizu ciparu
                        try:
                            new_price_str = input("Jaunā cena: > ").replace(',', '.')
                            price = float(new_price_str)
                            if price > 0:
                                set_price(name, price)
                                print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
                                break
                            else:
                                print("Cenai jābūt lielākai par 0!")
                        except ValueError:
                            print("Lūdzu, ievadiet derīgu skaitli!")
                    break # Izejam no A/M cikla
                else:
                    print("Lūdzu, ievadiet 'A' vai 'M'!")
        else:
            print("Cena nav zināma.")
            while True:
                try:
                    price_str = input("Ievadi cenu: > ").replace(',', '.')
                    price = float(price_str)
                    if price > 0:
                        set_price(name, price)
                        print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")
                        break
                    else:
                        print("Cenai jābūt lielākai par 0!")
                except ValueError:
                    print("Lūdzu, ievadiet derīgu skaitli!")
        
        # --- PIEVIENOT SARAKSTAM ---
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
    