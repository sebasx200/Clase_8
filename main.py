import problema1
from alumnos import alumnos


edad = 22
altura = 1.83
nombre = "Sebastián"
estado = True

lista_1 = [18, 22, 23, 12]
lista_2 = [1.83, 1.50, 1.66, 1.77]
lista_3 = ["Lunes", "Martes", "Miércoles"]
lista_4 = ["Sebastián", "22", 1.83, True]
if __name__ == '__main__':

    print(len(lista_1))
    print(len(lista_2))
    print(len(lista_3))
    print(len(lista_4))
    print()
    print (lista_1)
    lista_1[0] = 20
    print(lista_1)
    print(lista_1[0] + lista_1[3])
    print()
    problema1.sumar_5_enteros()
    print()
    alumnos()