import datetime
ma = datetime.date.today()
ev = ma.year

def bekeres():
    auto = input("Adja meg az autó nevét: ")
    gy_datum = int(input("Adja meg az autó gyártási dátumát: "))
    print("\nI/A:")
    print(f"\tAutó neve: {auto}")
    print(f"\tGyártási dátum: {gy_datum}")
    print("\nI/B:")
    if gy_datum == ev:
        eredmeny = "friss gyártás"
    elif gy_datum < 2000:
        eredmeny = "öreg autó"
    else:
        eredmeny = "átlagos autó"
    print(f"Ez a(z) {auto} {eredmeny}.")