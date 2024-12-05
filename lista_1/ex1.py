import pandas as pd
import random
import matplotlib.pyplot as plt

n = 40

def simulacao1():

    cont = 0

    caras = 0

    while caras < 3:
        lancameto = random.choice(['C', 'K'])

        cont += 1

        if lancameto == 'C':
            caras += 1;

    return cont


def exp1():

    resultados = []

    for _ in range(n):
        resultado = simulacao1()
        resultados.append(resultado)

    df = pd.DataFrame(resultados, columns=['Experimento1'])

    media = df.mean()
    moda = df.mode()
    mediana = df.median()
    variancia = df.var()

    print(df['Experimento1'].value_counts().sort_index())

    print(f"Média = {media}\nModa: {moda}\nMediana: {mediana}\nVariância: {variancia}")

    df['Experimento1'].hist(bins = 7, edgecolor = "black")

    plt.title('Distribuição do número de lançamentos')
    plt.xlabel('Lançamentos em até 3 caras consecutivas')
    plt.ylabel('Frequência')
    plt.show()

exp1()

def simulacao2():
    cont = 0
    caras = 0

    while cont < 6:
        cont += 1

        lancameto = random.choice(['C', 'K'])

        if lancameto == 'C':
            caras += 1
    
    return caras

def exp2():

    resultados = []

    for _ in range(n):
        res = simulacao2()
        resultados.append(res)

    df2 = pd.DataFrame(resultados, columns="Experimento2")

    media = df2.mean()
    moda = df2.mode()
    mediana = df2.median()
    variancia = df2.var()

    print(df2['Experimento2'].value_counts().sort_index())

    print(f"Média: {media}\nModa: {moda}\nMediana: {mediana}\nVariância: {variancia}")


exp2()
