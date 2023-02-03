import random

lista = []

def lotto():
    szamok = ""
    while len(lista) < 5:
        vel = int(random.random() * 90) + 1
        if len(lista) == 4:
            lista.append(vel)
            szamok += str(vel)
        else:
            lista.append(vel)
            szamok += str(vel) + "; "
    print("\nII/A, B, C:")
    print(f"\n \t{szamok}")

def egyjegyuek_szama():
    i = 0
    egyj_szama = 0
    while i < len(lista):
        if lista[i] < 10 and lista[i] > 0:
            egyj_szama += 1
        i += 1
    return egyj_szama

def konzol_kiir():
    print("\nII/D, E:")
    print(f"\n \tAz egyjegyűek száma: {egyjegyuek_szama()}.")

def file_kiir():
    fajl = open("szamok.txt", "w", encoding="utf-8")
    fajl.write(f"\nII/F: \n \n \tA fejek száma: {egyjegyuek_szama()}.")
    fajl.close()