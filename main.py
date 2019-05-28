from math import sin, pi


# x = dx*(indice_x + 1/2)
def calcula(K, alpha, Q, x, dx, dy, dt, cima, direita, baixo, esquerda, centro):
    
    V = alpha*sin(pi*x/5)
    U = alpha

    c2 = centro * ((2 * K) / (dy * dy) - 1 / dt + (2 * K) / (dx * dx))
    c3 = direita * (U / (2 * dx) - (K) / (dx * dx))
    c4 = esquerda * (- (U / (2 * dx)) - (K / dx * dx))
    c5 = cima * ( V / (2 * dy) - K / (dy * dy))
    c6 = baixo * ( - (V / (2 * dy)) - (K) / (dy * dy))
    c1 = -(c2 + c3 + c4 + c5 + c6 - Q/(dx*dy))*dt
    
    if c1 < 0:
        c1 = 0

    return c1

def faz_matriz(y, x, dy, dx, contorno):
    m = []
    qx = x/dx+1
    qy = y/dx+1
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



def main():
    print("---------- Analise de Difusao ----------")
    K = int(input("K: "))
    alpha = int(input("alpha: "))
    T = int(input("T: "))
    Q = int(input("Q: "))
    Lx = int(input("Lx: "))
    Ly = int(input("Ly: "))
    a = int(input("a: "))
    b = int(input("b: "))
    
#main()
