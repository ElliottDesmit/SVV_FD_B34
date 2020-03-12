# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:18:20 2020

@author: Vladimir
"""

import numpy as np
from get_excel_data import time, mass, fuel_used, m_f, M
import matplotlib.pyplot as plt
import math




cg_loc_crew = [131,131,170,214,214,251,251,288,288]     #inch - [1,2,10,3,4,5,6,7,8]
cg_loc_bag = [74,321,338]                               #inch   [nose, aft cabin,]
cg_loc_bem =  261.65                                          #inch
cg_loc_zfm = 0                       #inch
cg_loc_rm = 0                      #inch

# constants
BEM = 9165 * 0.453592  # kg
block_f = 4100 * 0.453592  # kg
c = [BEM,block_f]

def mass_funct(c, mass,time,fuel_used,t_i):      # sec

    
#    FFl = np.interp(t,time,ffl)
#    FFr = np.interp(t,time,ffr)
    t = np.arange(float(time[-1]))
    FU = np.interp(t,time,fuel_used)
    
    M_end= sum(c) + sum(mass) - FU[-1]
    M_t = sum(c) + sum(mass) - FU[math.ceil(t_i)]

    plt.plot(t,FU)
    plt.title("Fuel used in function of time")
    plt.show()

    return M_end, M_t

    
print(mass_funct(c,mass,time,fuel_used,0))



# def cg_funct():
#
#     num = sum(np.array(mass) * np.array(cg_loc_crew)) +  BEM * cg_loc_bem + Bag*cg_loc_bag + np.interp(Fuel , m_f,M)
#     den = sum (np.array(mass)) + BEM  +  Fuel  +  Bag
#
#     cg_loc = num / den
#
    
    
    
