import random as rd


def inicializar_matriz(matriz: list[list])->list[list]:

    posibles_marcas = [
        "Xiaomi", "Nubia", "Infinix", "Samsung"
    ]

    for i in range(20):
        posibles_marcas = rd.choice(posibles_marcas)       
        matriz[0].append(posibles_marcas)

        cantidad_elegida = rd.randint(10000,50000)
        matriz[1].append(cantidad_elegida)

        precio_unitario = rd.randrange(150000, 1200000) + (rd.randit(1, 100) / 100)
        matriz[2].append(precio_unitario)

        matriz[3].append(matriz[1][i] * matriz[2][i])

    return matriz

from depositos import matriz_datos

print(inicializar_matriz(matriz_datos))

