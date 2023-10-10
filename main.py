
print("Witaj w programie który zanalizuje twój tekst!")
text = input("Wpisz swój tekst:")

odwrócony_text = text[::-1]
ilosc_liter = len(text)
liczenie_powtorzen = []

licznik_powtorzen = {}
for litera in text:
    if litera.isalpha():  
        litera = litera.lower()  
        if litera in licznik_powtorzen:
            licznik_powtorzen[litera] += 1
        else:
            licznik_powtorzen[litera] = 1

for litera, ilosc in licznik_powtorzen.items():
    if ilosc > 1:
        print(f"Litera '{litera}' powtórzyła się {ilosc} razy.")


print(f"Ilość liter w twoim tekscie to: {ilosc_liter}")
print(f"Twój odrócony text to: {text[::-1]}")
