
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
block_f = 4050   # #lbs2676
Bag = 220   # lbs
c = [BEM,block_f,Bag]

def mass_funct(c, mass,time,fuel_used,DATA):      # sec


    t = np.arange(time[-1]+1)
    FU = np.poly1d(np.polyfit(np.array(time),np.array(fuel_used), 3))


    t_DATA = []
    FU_DATA = []
    for td in DATA[2:,20]:
        if td.isalpha():
            t_DATA.append(0)
        else:
            t_DATA.append((float(td)-40053.4237)/60)
    for ful,fur in zip(DATA[2:,14],DATA[2:,15]):
        FU_DATA.append(float(ful)+float(fur))

    correlation_matrix = np.corrcoef(fuel_used, FU(time))
    correlation_xy = correlation_matrix[0, 1]
    r_2 = correlation_xy ** 2


    M_beg= (sum(c) + sum(mass))  * 0.453592      #kg
    M_t_real = (np.ones(len(time))*(sum(c) + sum(mass)) - fuel_used)* 0.453592      #kg
    M_t_int = (np.ones(len(t))*(sum(c) + sum(mass)) - FU(t))* 0.453592      #kg
    M_t_DATA = np.ones(len(t_DATA))*(sum(c) + sum(mass))* 0.453592 - np.array(FU_DATA)      #kg
    # plt.scatter(time,M_t_real,marker='+')
    # plt.plot(t,M_t_int)
    plt.plot(time,M_t_real,linewidth = 1, marker = 'x', linestyle = "--")
    plt.grid()
    plt.xlabel("Time [min]")
    plt.ylabel("Aircraft mass [kg]")
    #plt.plot(t_DATA,M_t_DATA)
    plt.title("Aircraft mass in function of time" + str(r_2))
    plt.show()

    return M_t_DATA, FU(t), t, FU_DATA, t_DATA,time

M_t_DATA, x,x,x,x,x = mass_funct(c,mass,time,fuel_used,DATA)


def cg_funct(c, mass, time, fuel_used,CG,DATA):

    _, FU , t,_ , _,time = mass_funct(c, mass, time, fuel_used,DATA)


    num_noch = np.ones(len(fuel_used))*(sum(np.array(mass) * np.array(CG[0])) +  c[0] * CG[2] + c[2]*330) +  np.interp(np.ones(len(fuel_used))*c[1] - fuel_used, m_f,M) # bag included:
    den_noch = np.ones(len(fuel_used))*(sum(np.array(mass)) + c[0]  +  c[1] +c[2]) - fuel_used

    cg_loc_noch = num_noch / den_noch

    num = np.ones(len(FU)) * ( c[0] * CG[2] + c[2] * 330) + np.interp(np.ones(len(FU)) * c[1] - FU, m_f, M) + np.concatenate((sum(np.array(mass) * np.array(CG[0]))*np.ones(len(t[:-3])),sum(np.array(mass) * np.array(CG[3]))*np.ones(3)))
    den = np.ones(len(FU)) * (sum(np.array(mass)) + c[0] + c[1] + c[2]) - FU

    cg_loc = num / den

    num = np.ones(len(fuel_used)) * (c[0] * CG[2] + c[2] * 330) + np.interp(np.ones(len(fuel_used)) * c[1] - fuel_used, m_f,M) + np.concatenate((sum(np.array(mass) * np.array(CG[0])) * np.ones(len(time[:-2])), sum(np.array(mass) * np.array(CG[3])) * np.ones(2)))
    den = np.ones(len(fuel_used)) * (sum(np.array(mass)) + c[0] + c[1] + c[2]) - fuel_used

    cg_loc_real = num / den

    # plt.plot(t, cg_loc_noch,label = "no change")
    plt.plot(time, cg_loc_real*0.0254 , linewidth = 1, marker = 'x', linestyle = "--" )
    plt.title("CG loc in function of time")
    plt.ylabel("cg [m]")
    plt.xlabel("time [min]")
    plt.grid()
    plt.show()

    return cg_loc_noch[-3:]-cg_loc_real[-3:]

# print(cg_funct(c,mass,time,fuel_used,CG,DATA))




