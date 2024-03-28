# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:04:48 2023

@author: Alain FAUXCAS
"""

import numpy as np
import matplotlib.pyplot as plt
diction_data = {f'experience{i}': np.random.randn(110) for i in range(4)}
'''def graphe_data (donnee):
    plt.figure(figsize=(10,6))
    n = len(donnee)

    for k ,i in zip(donnee.values(),range(1,n+1)):
        plt.subplot(n,1,i)
        plt.plot(k)
        plt.title(f"experience{i}")
    plt.show()'''

def graphe(donnee):
    fig=plt.figure(figsize=(10,10))
    n=len(donnee)
    ax=fig.subplots(n,1)
    for i,k in zip(range(n),donnee.keys()):
        ax[i].plot(donnee[k])
        ax[i].set_title(k)
    plt.tight_layout()
    plt.show()
    
    

    

graphe(diction_data)

       