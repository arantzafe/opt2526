mes = 4

match mes:
    case 12 | 1 | 2:
        print("Invierno")
    case 3 | 4 | 5:
        print("Primave")
    case 6 | 7 | 8:
        print("Verano")
    case 9 | 10 | 11:
        print("Otoño")
    case _:
        print("Cualquier otro valor")