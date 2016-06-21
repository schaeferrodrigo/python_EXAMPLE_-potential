# -*- coding: utf-8 -*-
#=============================================
# goal : Plot the effective potential of two body problem
#=========================================================
import numpy as np
import matplotlib.pyplot as plt

def effective_potental_ext(r):
    """effective potential for the extrinsec case"""
    effec = 1/(r**2) - 2/r
    return effec

def effective_potental_int(r):
    """effective potencial for the intrinsec case"""
    effec = 1/(r**2) + np.log(r)
    return effec

def plot_pot(f,x_max,y_min,y_max,val_y):
    r = np.linspace(0.001,20,1000)
    plt.figure()
    plt.axis([0,x_max,y_min,y_max])
    plt.plot(r,f(r),linewidth = 1.5)
    plt.axhline(y = val_y, color = 'green', linewidth = 1.5)
    #plt.axhline(color = 'black')
    #plt.axvline()
    plt.yticks([])
    plt.xticks([])
    plt.show()

plot_pot(effective_potental_int,19,0,3,2)
#plot_pot(effective_potental_ext,5,-2,5,- 0.8)
