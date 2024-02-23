def unos_koordinata():
    while True:
        try:
            x1 = float(input("Unesite x koordinatu prve točke: "))
            y1 = float(input("Unesite y koordinatu prve točke: "))
            x2 = float(input("Unesite x koordinatu druge točke: "))
            y2 = float(input("Unesite y koordinatu druge točke: "))
            return x1, y1, x2, y2
        except ValueError:
            print("Pogrešan unos. Molimo Vas da unesite brojčane vrijednosti.")

def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Jednadžba pravca je x = {x1}")
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        print(f"Jednadžba pravca je y = {a}x + {b}")

def main():
    print("Unesite koordinate za dvije točke kako biste dobili jednadžbu pravca koja prolazi kroz njih.")
    x1, y1, x2, y2 = unos_koordinata()
    jednadzba_pravca(x1, y1, x2, y2)

if __name__ == "__main__":
    main()