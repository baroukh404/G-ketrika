# -*- coding: utf-8 -*-
"""
EXAMEN CALCUL NUMERIQUE : Mrs. Johary

@author: RABE-ANDRIAMAROZOKY ROVA HERVE
"""

# Imporatation du module numpy pour la representation matricielle
import numpy as np

# Importation du module matplolib pour la visualisation dans un plan (X, Y)
import matplotlib.pyplot as plt


class Interpolation:
    """
    Cette classe Interpolation sert à determiner les coefficients et tracer la courbe 
    sur l'interpolation de Newtion
    """

    def __init__(self, Xi, Yi):
        self.Xi = Xi
        self.Yi = Yi

    # Différence diviser de newton 
    def _fonction(self, X=[], Y=[]):
        data = []
        if len(X) > 2:
            numerateur = self._fonction(X[1:len(Xi)], Y[1:len(Y)])- self._fonction(X[0:len(X)-1], Y[0:len(X)-1])
            # print(numerateur)
            denominateur = X[-1]-X[0]
            data.append(numerateur/denominateur)
            # print(data)
            return np.array(data)
            
        else:
            if len(X) == 1:
                data.append(Y[-1])
                return np.array(data)
            else:
                numerateur = Y[-1]-Y[0]
                denominateur = X[-1]-X[0]
                data.append(numerateur/denominateur)
                # print(data)
                return np.array(data)

       
    def coefficient(self):
        """
        Determiner tous les coefficients du polynome de Newton.
        
        >> Xi = [1, 2, 3, 4, 5]
        >> Yi = [0.5, 1.2, 2, -2.5, 4.5]
        >> # Instancier un object Interpolation
        >> polynome = Interpolation(Xi, Yi)
        >> # afficher les coefficients
        >> polynome.coefficient()

        """
        # print(f'Nous avons un polynome de degree {len(self.Xi)}')
        print('Les coefficent du Polynome de Newton sont: ')
        stockage = []
        for i in range(len(self.Xi)):
            Ai = self._fonction(self.Xi[0:i+1], self.Yi[0:i+1])
            stockage.append(Ai.reshape(1,)[0])
            if stockage[i] == 0:
                pass
            else:
                print(f'A{i} =  {stockage[-1]}')
        return stockage

    def _coefficient(self):
        stockage = []
        for i in range(len(self.Xi)):
            Ai = self._fonction(self.Xi[0:i+1], self.Yi[0:i+1])
            stockage.append(Ai.reshape(1,)[0])
            # if stockage[i] == 0:
            #     pass
            # else:
                # print(f'A{i} =  {stockage[-1]}')
        return stockage




    # Methode qui sert à calculer les produits successifs dans le polynome de Newton. 
    def _prodX(self, X, Xi, n):
        """
        P0 = (X - X[0])
        P1 = (X - X[0])*(X - X[1])
        P2 = (X - X[0])*(X - X[1])*(X - X[2])
        ...
        Pn = (X - X[0])*(X - X[1])*...*(X - X[n])
        """
        p = 1
        for j in range(n+1):
            p = p*(X - Xi[j])
        return p

    # Connaissant déjà tous les coefficients Ai, On peut déterminer le polynôme de Newton.
    def _polynome(self):
        """
        S0 = Ai[0]
        S1 = Ai[0] + Ai[1]*(X - X[0])
        S2 = Ai[0] + Ai[2]*(X - X[0])*Ai[1]*(X - X[1])
        S3 = Ai[0] + Ai[3]*(X - X[0])*Ai[1]*(X - X[1])*(X - X[2])
        ... 
        Sn = Ai[0] + Ai[1]*(X - X[0])*Ai[1]*(X - X[1])*...*(X - X[n-1]) 
        """
        Ai = self._coefficient()
        S = Ai[0]
        for i in range(len(Ai)-1):
            S = S + Ai[i+1] * self._prodX(np.linspace(self.Xi[0], self.Xi[-1], 50), self.Xi, i)
        return S

    # Tracer la courbe et placer les points
    def courbe(self):
        plt.plot(np.linspace(self.Xi[0], self.Xi[-1], 50), self._polynome())
        plt.scatter(self.Xi, self.Yi)
        plt.show()

#########################################################################################################
#                                   TEST
#########################################################################################################

# =============================================================================
# TEST DE NOTRE CLASS INTERPOLATION DE NEWTON
# =============================================================================


# =============================================================================
# Vous pouvez entrer des valeurs de (Xi, Yi) i = 0,...,n
# Xi et Yi sont de même taille
# X0 < X1 < X2 < ... < Xn
# Xi = [1, 2, 3, 4, 5, 6]
# Yi = [-2, 1, 32, -5, 394, 893] 
# =============================================================================


Xi = [1, 2, 3, 4, 5, 6, 7]
Yi = [-1, 7, 60, 73, -2, 30, 5]

# Instanciation de l'Object Interpolation
polynome = Interpolation(Xi, Yi)

# Si je veux les coef. du polynome de Newton
polynome.coefficient()

# Si je veux tracer la courbe
polynome.courbe()




