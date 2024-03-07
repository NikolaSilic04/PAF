def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print("Jednadžba pravca: x =", x1)
    else:
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = y1 - nagib * x1
        print("Jednadžba pravca: y -", y1, "=", nagib, "* (x -", x1, ")")

# Poziv funkcije s primjerom koordinata točaka
jednadzba_pravca(1, 2, 3, 4)