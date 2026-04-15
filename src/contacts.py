import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contact(name, phone):
    """Pievieno jaunu kontaktu un saglabā failā."""
    contacts = load_contacts()
    # Pievieno sarakstam jaunu vārdnīcu
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"✓ Pievienots: {name} ({phone})")

def list_contacts():
    """Parāda visus saglabātos kontaktus."""
    contacts = load_contacts()
    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return
    
    print("Kontakti:")
    # enumerate(contacts, 1) ļauj smuki numurēt, sākot no 1
    for i, contact in enumerate(contacts, 1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")

def search_contacts(keyword):
    """Meklē kontaktu pēc vārda daļas (case-insensitive)."""
    contacts = load_contacts()
    # Filtrējam: pārbauda, vai meklētais vārds ir iekš kontakta vārda
    found = [c for c in contacts if keyword.lower() in c['name'].lower()]
    
    print(f"Atrasti {len(found)} kontakti:")
    for i, contact in enumerate(found, 1):
        print(f"  {i}. {contact['name']} — {contact['phone']}")

if __name__ == "__main__":
    # Pārbaudām, vai vispār ir ievadīta kāda komanda
    if len(sys.argv) < 2:
        print("Kļūda: Nav norādīta komanda (add, list, search)")
        sys.exit(1)
        
    command = sys.argv[1] # Paņem pirmo vārdu pēc 'contacts.py'
    
    if command == "add":
        # Pārbaudām, vai ir iedots vārds un numurs
        if len(sys.argv) < 4:
            print("Lūdzu norādiet vārdu un numuru pēdiņās!")
        else:
            name = sys.argv[2]
            phone = sys.argv[3]
            add_contact(name, phone)
            
    elif command == "list":
        list_contacts()
        
    elif command == "search":
        if len(sys.argv) < 3:
            print("Lūdzu norādiet meklējamo vārdu!")
        else:
            keyword = sys.argv[2]
            search_contacts(keyword)
            
    else:
        print(f"Nezināma komanda: {command}")
  

