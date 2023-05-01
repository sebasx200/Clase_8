def sumar_5_enteros():
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0
    while contadorWhile < tamano:
        lista.append(int(input("ingrese número " + str(contadorWhile) + ": ")))
        contadorWhile+= 1
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print(len(lista))
    print(lista)
    print(str(suma))

    for numero in lista:
        print(numero, end=', ')
    print("\nLa suma de sus elementos es: ")
    print(suma)

if __name__ == '__main__':

    sumar_5_enteros()

