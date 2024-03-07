import matplotlib.pyplot as plt

def jednadzba_pravca(x1, y1, x2, y2, ime_pdf=None):
    if x1 == x2:
        print("Jednadžba pravca: x =", x1)
    else:
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = y1 - nagib * x1
        print("Jednadžba pravca: y -", y1, "=", nagib, "* (x -", x1, ")")

    
        plt.plot([x1, x2], [y1, y2], 'ro', label='Točke')
        
        x_values = [x1, x2]
        y_values = [nagib * x + slobodni_clan for x in x_values]
        plt.plot(x_values, y_values, label='Pravac')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graf pravca kroz točke')
        plt.legend()

        if ime_pdf:
            plt.savefig(ime_pdf + '.pdf')
            print(f"Graf je spremljen kao {ime_pdf}.pdf")
        else:
            plt.show()

jednadzba_pravca(1, 2, 3, 4, ime_pdf="pravac_kroz_tocke")