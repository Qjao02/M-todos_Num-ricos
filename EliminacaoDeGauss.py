def read_matriz_file():
    file = open('input/matriz.txt','r')
    dimension = int(file.readline().replace('\n', ''))
    matriz = []
    for line in file.readlines():
        line = line.replace('\n','')
        row = list(map(int, line.split(' ')))
        matriz.append(row)
    return dimension, matriz

def read_vetor_file():
    file = open('input/vetor.txt','r')
    vetor = file.readline().split(' ')
    return vetor

def eliminacao_gauss(matriz, dimensao):
    b = []
    x = []
    for i in range(dimensao):
        b.append(1)
        x.append(1)

    for k in range(0, dimensao - 1  ):
        i = k+1
        for i in range(k+1, dimensao ):
            m = matriz[i][k]/matriz[k][k]
            matriz[i][k] = 0
            j = k+1
            for j in range(k+1, dimensao):
                matriz[i][j] = matriz[i][j] - (m * matriz[k][j])

            b[i] = b[i] - m * b[k]


    x[dimensao - 1] = b[dimensao-1] / matriz[dimensao-1][dimensao-1]
    for i in range(0, dimensao-1, -1):
        soma = 0
        j = i + 1
        for j in range(i+1, dimensao):
            soma += matriz[i][j] * x[j]

        x[i] = (b[i] - soma)/matriz[i][i]

    return x, matriz



def gaussSeidel(matriz, b, tol ,dimensao, n, x_prox):
    k = 0
    for k in range(0,dimensao):
        for i in range(dimensao):
            alpha = 0
            for j in range(i-1):
                alpha += matriz[i][j] x[j]
            j = i+1
            for j in range(i+1,dimensao):
                alpha = alpha + a[i][j] * b[i]



if __name__ == "__main__":
    dimensao, matriz = read_matriz_file()
    b = read_vetor_file()
    #print(dimensao, matriz)

    #resposta para eliminação de gauss
    response, matriz_escalonada = eliminacao_gauss(matriz, dimensao)
    #print(response)
    #print(matriz_escalonada)

    #resposta para gauss seidel
    vetor = read_vetor_file()
    print(vetor)