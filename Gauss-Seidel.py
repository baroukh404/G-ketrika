# -*- coding: utf-8 -*-
"""
EXAMEN CALCUL NUMERIQUE : Mrs. Johary

@author: RABE-ANDRIAMAROZOKY ROVA HERVE
"""


# Importer le module numpy pour faire la représentation matricielle
import numpy as np

class SystemLinaire:
    def __init__(self, A, B):
        """
        Résout le système linéaire Ax=b par la méthode de Gauss-Seidel avec une approximation initiale x0.
    
        Arguments :
        A -- la matrice du système linéaire
        B -- le vecteur du second membre du système linéaire
        
        Pour que la méthode de Gauss converge vers la solution,
        - la matrice A doit être une matrice à diagonale strictement
        dominante
        
        |A[i][j]| > sum |A[i][j]| pour j != i
        
        i.e : 
        - la matrice A est une matrice symetrique definie positive
        
        i.e : A.T == A
            
        Retourne :
        La solution du système linéaire
        """
        self._A = A
        self._B = B
        self._taille = len(B)
        self._initialisation = np.zeros(self._taille)
        self._epsilon = 0.00001
        self._iterationMax = 1000
        self._x = self._initialisation.copy()
        
    def GaussSeidel(self):
        iteration = self._iterationMax
        try:
            for k in range(iteration):
                for i in range(self._taille):
                    self._x[i] = (b[i] - np.dot(A[i,:i], self._x[:i]) - np.dot(A[i,i+1:], self._initialisation[i+1:])) / A[i,i]
                if np.linalg.norm(self._x - self._initialisation) < self._epsilon:
                    return self._x
                self._initialisation = self._x.copy()
            
            raise Exception()
            
        except:
            print('Veillez vérifier votre matrice carré :')
            text = r"""
            Pour que la méthode de Gauss converge vers la solution,
            - la matrice A doit être une matrice à diagonale strictement
            dominante
            
            |A[i][j]| > sum |A[i][j]| pour j != i
            
            i.e : 
            - la matrice A est une matrice symetrique definie positive
            
            i.e : A.T == A"""
            print(text)


# =============================================================================
#                           TEST DE NOTRE CLASS
# =============================================================================

A = np.array([
    [9, 4, 1],
    [1, 6, 0],
    [1, -2, -6]
    ])

b = np.array([-17, 4, 14])

print('\nSolution approché par notre class')
x = SystemLinaire(A, b)
print(x.GaussSeidel(), '\n')

# =============================================================================
# VERIFICATION EN UTILISANT DES METHODE PREDEFINIE DANS NUMPY
# =============================================================================

print('Verification par méthode de résolution prédéfinie dans numpy : ')
x = np.linalg.solve(A, b)
print(x)



