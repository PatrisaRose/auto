from Auto import Auto
lista = []
def beolvasas():
    fajl = open("auto.txt", "r", encoding="utf-8")
    fejlec = fajl.readline()
    sorok = fajl.readlines()
    fajl.close()

    i = 0
    while len(sorok) > i:
        sor = sorok[i].strip().split("$")
        lista.append(Auto(sor))
        i += 1

def flotta():
    i = 0
    c = 0
    while i < len(lista):
        if lista[i].auto:
            c += 1
        i += 1
    print("\nIII/Flotta:")
    print(f"\n \tAutók száma: {c}.")
    return c

def legfiatalabb():
    i = 0
    max = lista[0].datum
    max_index = 0
    while i < len(lista):
        if lista[i].datum > max:
            max = lista[i].datum
            max_index = i
        i += 1
    print("\nIII/Legfiatalabb:")
    print(f"\n \tA legfiatalabb autó: {lista[max_index].auto}({max}))")

