import numpy as np
import matplotlib.pyplot as plt

        
class interpolation:
    def __init__(self, Xi, Yi):
        self.Xi = np.array(Xi)
        self.Yi = np.array(Yi)
        self.FX = 0
        
    def _fonction(self, X, Y):
        """
        Difference diffiser de newton pour contruire le polynome de newton.
        """
        data = []
        if len(X) > 2:
            numerateur = self._fonction(X[1::], Y[1::]) - self._fonction(X[0:len(X)-1], Y[0:len(X)-1])
            denominateur = X[-1]-X[0]
            data.append(numerateur/denominateur)
            return np.array(data)         
        else:
            if len(X) == 1:
                data.append(Y[-1])
                return np.array(data)
            else:   
                numerateur = Y[-1]-Y[0]
                denominateur = X[-1]-X[0]
                data.append(numerateur/denominateur)
                return np.array(data)
            
            
    def coefficient(self):
        """
        cette fonction sert a determiner tous le coefficent du polynome
        """
        stockage = []
        for i in range(len(self.Xi)):
            Ai = self._fonction(self.Xi[0:i+1], self.Yi[0:i+1])
            stockage.append(Ai.reshape(1,)[0])
            # if stockage[i] == 0:
            #     pass
            # else:
            #     print(f'A{i} =  {stockage[-1]}')
        return stockage
    
    
    def conversion(self):
        """
        Convertir les données en entrée en une liste
        """
        stockage = []
        self.Xi  = self.Xi.replace(']', '')
        self.Xi  = self.Xi.replace('[', '')
        self.Xi = self.Xi.split(',')
        for i in range(len(self.Xi)):
            stockage.append(float(self.Xi[i]))
    
        # convertir notre variable en matrice
        stockage = np.array(stockage)
        return stockage
    

    def courbe(self, polynome_newton):
        """
        Appel cette méthode pour tracer la courbe
        """
        self.FX = polynome_newton
        plt.plot(np.linspace(self.Xi[0], self.Xi[-1], 50), self.FX)
        plt.scatter(self.Xi, self.Yi)
        plt.show()


if __name__ == '__main__':
    # Xi = input('Entrer les valeurs de xi dans une liste: ')
    # print(Xi)
    # Xi = conversion(Xi)
    # Yi = input('Entrer les valeurs de yi dans une liste: ')
    # Yi = conversion(Yi)
    Xi = [1, 2.5, 3, 4]
    Yi = [81, 70, 42, 81]
    points = interpolation(Xi, Yi)
    Ai = points.coefficient()
    
    X = np.linspace(Xi[0], Xi[-1], 50)
    S = Ai[0]
    S = S + Ai[1]*(X - Xi[0])
    S = S + Ai[2]*(X - Xi[0])*(X - Xi[1])
    S = S + Ai[3]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])
    # S = S + Ai[4]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])*(X - Xi[3])
    # S = S + Ai[5]*(X - Xi[0])*(X - Xi[1])*(X - Xi[2])*(X - Xi[3])*(X - Xi[4])
    points.courbe(S)