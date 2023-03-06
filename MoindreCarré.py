# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:24:31 2023

@author: baroukh404
"""

import numpy as np
import matplotlib.pyplot as plt

# Définition de notre class Moindre Carré

class MoindreCarre:
    """
    Réalise une régression linéaire à partir des données x et y en utilisant la méthode des moindres carrés.

    Arguments :
    x -- le vecteur des données x
    y -- le vecteur des données y

    Retourne :
    Les coefficients a et b de la droite de régression linéaire y = a*x + b
    """
    def __init__(self, Xi, Yi):
        self._Xi = Xi
        self._Yi = Yi
        self._taille = len(self._Xi)
    
    # Il existe différent type de méthode mais notre sujet c'est la regréssion linéaire
    def RegrLineaire(self):
        x_mean = np.mean(self._Xi)
        y_mean = np.mean(self._Yi)
        xy_mean = np.mean(self._Xi * self._Yi)
        x_squared_mean = np.mean(self._Xi**2)
        a = (xy_mean - x_mean * y_mean) / (x_squared_mean - x_mean**2)
        b = y_mean - a * x_mean
        return [a, b]
    

# =============================================================================
# APPLICATION DE NOTRE CLASS MOINDRECARRE-REGRESSION LINEAIRE
# =============================================================================

# Prendre aleatoirement la valeur de Xi, Yi
x = np.arange(0, 100, 7.5)
y = np.random.randint(0, 100, len(x))

# Creation de notre Object MoindreCarre
fonction = MoindreCarre(x, y)

# Appel sur la methode de regression lineaire de notre class MoindreCarre
Droite = fonction.RegrLineaire()

# a, b = linear_regression(x, y)
print("Coefficients de la droite de régression : a = {:.3f}, b = {:.3f}".format(Droite[0], Droite[-1]))

# Notre droite Y = AX + B peut se presenter comme suit:
Y = Droite[0]*x + Droite[-1]

# Placement de tous les points (Xi, Yi)
plt.scatter(x, y)

# Tracer la droite de Regression Lineaire
plt.plot(x, Y)

