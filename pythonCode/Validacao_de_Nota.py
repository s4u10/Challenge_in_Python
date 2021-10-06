def notas_media(x, y):
    media = (x + y) / 2
    print(f"media = {media:.2f}")


def notas_validas():
    x = float(input("Informar o valor da nota: "))

    if 0 <= x <= 10:
        return x
    else:
        print('nota invalida')
        return notas_validas()


choice = 1
while choice == 1:
    j = -1
    k = -1

    while j == -1:
        j = notas_validas()

    while k == -1:
        k = notas_validas()

    notas_media(j, k)
    choice = 3

    while choice != 1 and choice != 2:
        choice = eval(input('novo calculo (1-sim 2-nao)\n'))