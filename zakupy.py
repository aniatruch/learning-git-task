zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

suma_produktow = 0
for sklep, produkty in zakupy.items():
    print(f"Idę do {sklep.capitalize()} i kupuję tam {', '.join([produkt.capitalize() for produkt in produkty])}.")
    suma_produktow += len(produkty)

print(f"W sumie kupuję {suma_produktow} produktów.")
print()
print("Hello")
print("Piękna dziś pogoda")
print ("Nie trzeba nosić parasola, bo nie pada deszcz")