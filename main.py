from math import sin, pi
from copy import deepcopy
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import os

def faz_matriz(y, x, dy, dx):
    m = []
    qx = x/dx+1
    qy = y/dy+1
    for i in range(int(qx)):
        l = []
        for j in range(int(qy)):
            """
            if i == 0:
                l.append(contorno[0])
            elif i == qx-1:
                l.append(contorno[2])
            elif j == 0:
                l.append(contorno[3])
            elif j == qy-1:
                l.append(contorno[1])
            else:
                l.append(0)
            """
            l.append(0)
        m.append(l)

    return m

# x = dx*(indice_x + 1/2)
def calcula_ponto(K, alpha, q, x, dx, dy, dt, cima, direita, baixo, esquerda, centro):
    
    V = alpha*sin(pi*x/5)
    U = alpha

    c2 = centro * ((2 * K) / (dy * dy) - 1 / dt + (2 * K) / (dx * dx))
    c3 = esquerda * (U / (2 * dx) - (K) / (dx * dx))
    c4 = direita * (- (U / (2 * dx)) - (K / dx * dx))
    c5 = cima * ( V / (2 * dy) - K / (dy * dy))
    c6 = baixo * ( - (V / (2 * dy)) - (K) / (dy * dy))
    c1 = -(c2 + c3 + c4 + c5 + c6 - q/(dx*dy))*dt
    
    if c1 < 0:
        c1 = 0

    return c1

def calcula_matriz(matriz, K, alpha, Q, a, b, T, dx, dy, dt):
    c_max = 0
    
    xa = 1 + int(a/dx)
    yb = 1 + int(b/dy)

    t = 0
    count = 0

    while (t < 10*T):

        n_matriz = deepcopy(matriz)

        for j in range(len(matriz)):
            for i in range(len(matriz[0])):

                # Geração
                if t < T and i == xa and j == yb:
                    q = Q/(dx*dy)
                    x = dx * (i + 1 / 2)
                    cima = matriz[j-1][i]
                    direita = matriz[j][i+1]
                    baixo = matriz[j+1][i]
                    esquerda = matriz[j][i-1]
                    centro = matriz[j][i]
                    n_matriz[j][i] = calcula_ponto(K, alpha, q, x, dx, dy, dt, cima, direita, baixo, esquerda, centro)
                    if n_matriz[j][i] > c_max:
                        c_max = n_matriz[j][i]
                else:
                    q = 0
                    #Condições de contorno
                    if i == 0:
                        n_matriz[j][i] = matriz[j][i+1]

                    elif i == (len(matriz[0])-1):
                        n_matriz[j][i] = matriz[j][i-1]

                    elif j == 0:
                        n_matriz[j][i] = matriz[j+1][i]
                        
                    elif j == (len(matriz)-1):
                        n_matriz[j][i] = matriz[j-1][i]

                    #Caso geral
                    else:
                        x = dx * (i + 1 / 2)
                        cima = matriz[j-1][i]
                        direita = matriz[j][i+1]
                        baixo = matriz[j+1][i]
                        esquerda = matriz[j][i-1]
                        centro = matriz[j][i]

                        n_matriz[j][i] = calcula_ponto(K, alpha, q, x, dx, dy, dt, cima, direita, baixo, esquerda, centro)
                        if n_matriz[j][i] > c_max:
                            c_max = n_matriz[j][i]

        matriz = n_matriz
        t += dt

        # A cada 10 steps, guarda uma foto
        if ((t // dt)%10) == 0:
            ax = sns.heatmap(matriz)
            ax.invert_yaxis()
            plt.savefig("img/f"+str(count)+".png")
            plt.clf()

        count += 1
    print(c_max)
    return matriz




def main():
    
    print("---------- Analise de Difusao ----------")
    K = float(input("K: "))
    alpha = float(input("alpha: "))
    Q = float(input("Q: "))
    Lx = float(input("Lx: "))
    Ly = float(input("Ly: "))
    dx = float(input("dx: "))
    dy = float(input("dy: "))
    a = float(input("a: "))
    b = float(input("b: "))
    T = float(input("T: "))
    # dt baseado na condição de convergência
    dt = 0.2*((dx*dy)/(4*K))

    arqs = os.listdir("C:/Users/LiuSeeker/Desktop/5o-semestre/TermoSol/APS5-TransCal/img/")
    for arq in arqs:
        if arq.endswith(".png"):
            os.remove(os.path.join("C:/Users/LiuSeeker/Desktop/5o-semestre/TermoSol/APS5-TransCal/img/", arq))
    matriz = faz_matriz(Ly, Lx, dy, dx)
    n_matriz = calcula_matriz(matriz, K, alpha, Q, a, b, T, dx, dy, dt)
    
main()
