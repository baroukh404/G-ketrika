import numpy as np
import matplotlib.pyplot as plt

def fonction(Xi=[], Yi=[]):
    """
    Difference diffiser de newton pour contruise le polynome de newton.
    """
    data = []
    if len(Xi) > 2:
        numerateur = fonction(Xi[1:len(Xi)], Yi[1:len(Yi)])-fonction(Xi[0:len(Xi)-1], Yi[0:len(Xi)-1])
#         print(numerateur)
        denominateur = Xi[-1]-Xi[0]
        data.append(numerateur/denominateur)
#         print(data)
        return np.array(data)
        
    else:
        if len(Xi) == 1:
            data.append(Yi[-1])
            return np.array(data)
        else:
            numerateur = Yi[-1]-Yi[0]
            denominateur = Xi[-1]-Xi[0]
            data.append(numerateur/denominateur)
    #         print(data)
            return np.array(data)
        
def coefficient(Xi, Yi):
    """
    cette fonction sert a determiner tous le coefficent du polynome
    """
    stockage = []
    for i in range(len(Xi)):
        Ai = fonction(Xi[0:i+1], Yi[0:i+1])
        stockage.append(Ai.reshape(1,)[0])
        if stockage[i] == 0:
            pass
        else:
            print(f'A{i} =  {stockage[-1]}')
    return stockage

def conversion(Xi):
    """
    fonction pour convertir une chaine de caractere comme '[1, 2, 2]' en une liste [1, 2, 3]
    """
    stockage = []
    Xi  = Xi.replace(']', '')
    Xi  = Xi.replace('[', '')
    Xi = Xi.split(',')
    for i in range(len(Xi)):
        stockage.append(int(Xi[i]))

    # convertir notre variable en matrice
    stockage = np.array(stockage)
    return stockage

def courbe(Xi, Yi, polynome_newton):
    """
    Tracer la courbe et les points
    """
    plt.plot(np.linspace(Xi[0], Xi[-1], 50), polynome_newton)
    plt.scatter(Xi, Yi)
    plt.show()

if __name__ == '__main__':
    Xi = input('Entrer les valeurs de xi dans une liste: ')
    # print(Xi)
    Xi = conversion(Xi)
    Yi = input('Entrer les valeurs de yi dans une liste: ')
    Yi = conversion(Yi)

    Ai = coefficient(Xi, Yi)
    print(type(Ai))
    X = np.linspace(Xi[0], Xi[-1], 50)
    S = Ai[0]
    S = S + Ai[1]*(X - Xi[0])
    S = S + Ai[2]*(X - Xi[0])*(X - Xi[1])
    S = S + Ai[3]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])
    S = S + Ai[4]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])*(X - Xi[3])
    S = S + Ai[5]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])*(X - Xi[3])*(X - Xi[4])
    courbe(Xi, Yi, S)