# Ispisi brojeve od 1 do 5
# Ispisi svako slovo iz peci Python
# Odbrojavanje u while petlji od 5 do 1
# Napisi iteraciju kroz listi, a lista sadrzi reci crvena, zelena i plava
# While petlja unosi dok korisnik ne prekine

# Zadatak 1
print("Zadatak1\n")
for i in range (1, 6):
    print(i)

# Zadatak 2
print("Zadatak2\n")
for slovo in "Python":
    print(slovo)

# Zadatak 3
print("Zadatak3\n")

broj = 5
while broj > 0:
    print(broj)
    broj -= 1

br = 2
while br <= 10:
    print(br)
    br += 1

# Zadatak 4
print("Zadatak4\n")

boje = ["crvena", "zelena", "plava"]
for boja in boje:
    print(boja)

drnch = [1, "kurac", 5463, [1, 2]]
for drk in drnch:
    print(drk)
    print(drnch)

# Zadatak 5
print("Zadatak5\n")

unos = ""

while unos != "stop":
    unos = input("unesi nesto (ili 'stop' za kraj): ")


