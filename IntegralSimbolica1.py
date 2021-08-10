# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:09:35 2021

@author: Samaung
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import sympy as sp

x1=np.arange(0.1, 10, 0.5)
y=-x1+np.random.normal(0,0.5,20)

t, K, x = sp.symbols('t K x')
g=sp.integrate(t*K/x, (x, 1, 10))
f=sp.lambdify((t,K), g)

parametros, erro = curve_fit(f, x1, y)
xFit=np.arange(0, 10, 0.01)
plt.plot(xFit, f(xFit, *parametros))
print("K =", parametros[0])
print("Mat Cov =", erro)
plt.plot(x1, y, 'o')

