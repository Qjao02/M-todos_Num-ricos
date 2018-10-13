import sys
def read_matriz_file():
    file = open('input/matriz_exercicio_caderno.txt','r')
    dimensao = int(file.readline().replace('\n', ''))
    matriz = []
    rows = file.read().splitlines()
    for line in rows:
        matriz.append(list(map(float,line.split(' '))))

    return dimensao, matriz

def read_vetor_file():
    file = open('input/vetor_exercicio_caderno.txt','r')
    vetor = list(map(float, file.readline().split(' ')))
    return vetor

def eliminacao_gauss(matriz, dimensao, b):
    x = []
    for i in range(dimensao):
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
    for i in range(dimensao-2, -1, -1):
        soma = 0
        for j in range(i+1, dimensao):
            soma = soma + matriz[i][j] * x[j]

        x[i] = (b[i] - soma)/matriz[i][i]

    return x, matriz


def calc_erro(x_atual,x_ant):
    num = []
    for i in range (len(x_atual)):
        num.append(abs(x_atual[i] - x_ant[i]))

    err = max(num)/max(x_atual)
    print('erro' + str(err))
    return err


def gaussSeidel(matriz, b, tol , stop ):

    x_ant = []
    x_atual = []
    for i in range(len(b)):
        x_ant.append(1)
        x_atual.append(1)

    k = 1
    while(k <= stop):
        for i in range(0, len(b)):
            alpha = 0
            for j in range(1, i):
                alpha = alpha + matriz[i][j] * x_atual[j]
            for j in range(i+1, len(b)):
                alpha = alpha + matriz[i][j] * x_ant[j]
            x_atual[i] = (b[i] - alpha) / matriz[i][i]

        if( calc_erro(x_atual,x_ant) < tol):
            return x_atual
        x_ant = x_atual
        k = k+1

    print('numero de iteracoes expirados')
    return x_atual

if __name__ == "__main__":
    dimensao, matriz = read_matriz_file()
    b = read_vetor_file()

    #resposta para eliminação de gauss
    response, matriz_escalonada = eliminacao_gauss(matriz, dimensao, b)
    print(response)
    print(matriz_escalonada)

    '''
    response, matriz_escalonada = eliminacao_gauss(matriz, dimensao)
    #resposta para gauss seidel
    vetor = read_vetor_file()
    print(vetor)

    response = gaussSeidel(matriz, vetor, 0.004, 2)
    print('response for gauss seidel' + str(response))
    '''