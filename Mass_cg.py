
import numpy as np
from XCl_get_mass_cg import time, mass, fuel_used, m_f, M
import matplotlib.pyplot as plt
import math
from Fligth_Data import DATA




cg_loc_crew = [131,131,170,214,214,251,251,288,288]   #inch - [1,2,10,3,4,5,6,7,8]
cg_new = [131,131,170,214,214,251,251,288,131]
cg_loc_bag = [74,321,338]                               #inch   [nose, aft cabin,]
cg_loc_bem =  291.65                                          #inch
cg_loc_zfm = 0                       #inch
cg_loc_rm = 0                      #inch
CG = [cg_loc_crew, cg_loc_bag,cg_loc_bem,cg_new]

# constants
BEM = 9165  # lbs
block_f = 2676   # #lbs
Bag = 220   # lbs
c = [BEM,block_f,Bag]

def mass_funct(c, mass,time,fuel_used,t_i,DATA):      # sec

    
#    FFl = np.interp(t,time,ffl)
#    FFr = np.interp(t,time,ffr)
    t = np.arange(float(time[-1])+1)
    FU = np.interp(t,time,fuel_used)

    t_DATA = []
    FU_DATA = []
    for td in DATA[2:,20]:
        if td.isalpha():
            t_DATA.append(0)
        else:
            t_DATA.append((float(td)-33452.0962)/60)
    for ful,fur in zip(DATA[2:,14],DATA[2:,15]):
        FU_DATA.append(float(ful)+float(fur))
    
    M_end= (sum(c) + sum(mass) - FU[-1])  * 0.453592      #kg
    M_t = (sum(c) + sum(mass) - FU[math.ceil(t_i)])       #kg
    plt.plot(t,FU* 0.453592)                            #kg
    plt.plot(t_DATA,FU_DATA)
    plt.title("Fuel used in function of time")
    plt.show()

    return M_end, M_t , FU , t

    




def cg_funct(c, mass, time, fuel_used, t_i,CG,DATA):

    _ , _, FU , t = mass_funct(c, mass, time, fuel_used, t_i,DATA)

    num_noch = np.ones(len(FU))*(sum(np.array(mass) * np.array(CG[0])) +  c[0] * CG[2] + c[2]*330) +  np.interp(np.ones(len(FU))*c[1] - FU, m_f,M) # bag included:
    den_noch = np.ones(len(FU))*(sum(np.array(mass)) + c[0]  +  c[1] +c[2]) - FU

    cg_loc_noch = num_noch / den_noch

    num = np.ones(len(FU)) * ( c[0] * CG[2] + c[2] * 330) + np.interp(np.ones(len(FU)) * c[1] - FU, m_f, M) + np.concatenate((sum(np.array(mass) * np.array(CG[0]))*np.ones(len(t[:-3])),sum(np.array(mass) * np.array(CG[3]))*np.ones(3)))
    den = np.ones(len(FU)) * (sum(np.array(mass)) + c[0] + c[1] + c[2]) - FU

    cg_loc = num / den

    plt.plot(t, cg_loc_noch,label = "no change")
    plt.plot(t, cg_loc,label = " change")
    plt.title("CG loc in function of time")
    plt.ylabel("cg in inch")
    plt.xlabel("time [min]")
    plt.legend()
    plt.show()

    return cg_loc_noch[math.ceil(t_i)],cg_loc[math.ceil(t_i)], (cg_loc_noch-cg_loc)[-4:]

print(cg_funct(c,mass,time,fuel_used,41,CG,DATA))




