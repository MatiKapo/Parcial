

lista_1 = []
lista_2 = []
lista_3 = []

listas = [lista_1, lista_2, lista_3]

def cargar_marca(numero: int)->None:
    for i in listas:
        numero = int(input('ingrese unidades: '))
        listas[i].append(numero)
        

if __name__ == '__main__':

    cargar_marca(50)

    