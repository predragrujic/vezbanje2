#  u listi od 1 do 5 i ispisi za svaki da li je paran ili ne
# U listi reci koja sadrzi stringove pas, automobil, sunce i kisa, svaka rec koja je duza od 4 slova ispisi rec - duga rec ili za menje - kratka rec
# Lista brojeva 3,15,8,21,7, svaki boj testiraj dal je veci od 10 istisi je veci od 10 ili broj nije veci od 10
# Lista -2,5,0,-7,9, ispisi da li je broj pozitivan, negativan ili nula
# Testiraj da li u listi 13,24,30,42  da li element sadrzi cifru 3..i ako sadrzi ispisi sadrzi i ako ne sadrzi, napisi ne sadrzi

print("vezba1\n")

for broj in range(1, 6):
    if broj % 2 == 0:
        print(broj, " je paran")
    else:
        print(broj, " je neparan")

print("vezba2\n")

reci = ["pas", "automobil", "sunce", "kisa"]
for rec in reci:
    if len(rec) > 4:
        print(f"{rec} - duga rec")
    else:
        print(f"{rec} - kratka rec")

print("vezba3\n")

brojevi = [3, 15, 8, 21, 7]
for broj in brojevi:
    if broj > 10:
        print(f"{broj} - je veci od 10")
    else:
        print(f"{broj} - je manji od 10")

print("vezba4\n")

lista_br = [-2, 5, 0, -7, 9]
for br in lista_br:
    if br > 0:
        print(f"{br} - pozitivan broj")
    elif br < 0:
        print(f"{br} - negativan broj")
    else:
        print(f"{br} - je nula")

print("vezba5\n")

for broj in [13, 24, 30, 42]:
    if "3" in str(broj): # konvertuje 13 u "13"
        print(f"{broj} - sadrzi cifru 3")
    else:
        print(f"{broj} - nesadrzi cifru 3")
