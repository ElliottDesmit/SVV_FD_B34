# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:56:55 2020

@author: Elliott
"""

# Script for the Eigenmode Plots from the Flight Test Data
#=========================================================
#=========================================================

# Imports
#========
import numpy as np
import matplotlib.pyplot as plt
from Flight_Data import DATA

# function to fix the mess
#=========================
def fixit(arr) :
    arr_n = np.zeros(arr.shape)
    for i in range(arr.shape[0]):
        arr_n[i] = float(arr[i])
    return arr_n    

# create all flight parameter arrays
#===================================
alpha0 = 1.4 / 180 * np.pi
th0 = alpha0

t = fixit(DATA[2:,48]) # time array
u_val = fixit(DATA[2:,41]) - fixit(DATA[2:,42]) # speed deviation experimental [m/s]
alpha_val = fixit(DATA[2:,0])  - (180 * alpha0 / np.pi) # AoA experimental [deg]
theta_val = fixit(DATA[2:,22])  - (180 * th0 / np.pi) # th experimental [deg]
q_val = fixit(DATA[2:,27]) # q experimental [deg/s]
phi_val = fixit(DATA[2:,21]) # `roll angle experimental [deg]
p_val = fixit(DATA[2:,26]) # roll rate experimental [deg/s]
r_val = fixit(DATA[2:,28]) # yaw rate experimental [deg/s]

# Start and end times of each eigenmode
#======================================
t_aperiodic = np.arange(2711,2750,0.1)
t_shortperiod = np.arange(2766,2771,0.1)
t_dutch = np.arange(2850,2880,0.1)
t_yaw = np.arange(2919,2949,0.1)
t_phugoid = np.arange(2975,3128,0.1)
t_spiral = np.arange(3400,3470,0.1)

# Symmetric
#==========

###1 Short period
##b , e = list(t).index(2766) , list(t).index(2770)
##
##plt.subplot(221)
##plt.grid()
##plt.title("Deviation from Nominal Speed", fontsize="20")
##plt.plot(t_shortperiod,u_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Speed [m/s]", fontsize="15")
##plt.legend()
##plt.subplot(222)
##plt.grid()
##plt.title("Angle of Attack", fontsize="20")
##plt.plot(t_shortperiod,alpha_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(223)
##plt.grid()
##plt.title("Pitch Angle", fontsize="20")
##plt.plot(t_shortperiod,theta_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(224)
##plt.grid()
##plt.title("Pitch rate", fontsize="20")
##plt.plot(t_shortperiod,q_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angular Speed [deg/s]", fontsize="15")
##plt.legend()
##
###plt.show()
##
##
###2 Phugoid
##b , e = list(t).index(2975) , list(t).index(3128)
##
##plt.subplot(221)
##plt.grid()
##plt.title("Deviation from Nominal Speed", fontsize="20")
##plt.plot(t_phugoid,u_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Speed [m/s]", fontsize="15")
##plt.legend()
##plt.subplot(222)
##plt.grid()
##plt.title("Angle of Attack", fontsize="20")
##plt.plot(t_phugoid,alpha_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(223)
##plt.grid()
##plt.title("Pitch Angle", fontsize="20")
##plt.plot(t_phugoid,theta_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(224)
##plt.grid()
##plt.title("Pitch Rate", fontsize="20")
##plt.plot(t_phugoid,q_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angular Speed [deg/s]", fontsize="15")
##plt.legend()
##
###plt.show()
##
###Asymmetric
###==========
##
###1 Aperiodic
##b , e = list(t).index(2711) , list(t).index(2750)
##
##plt.subplot(221)
##plt.grid()
##plt.title("Roll Angle", fontsize="20")
##plt.plot(t_aperiodic,phi_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(222)
##plt.grid()
##plt.title("Roll Rate", fontsize="20")
##plt.plot(t_aperiodic,p_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##plt.subplot(212)
##plt.grid()
##plt.title("Yaw Rate", fontsize="20")
##plt.plot(t_aperiodic,r_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##
###plt.show()
##
###2 dutch
##b , e = list(t).index(2850),list(t).index(2880)
##
##plt.subplot(221)
##plt.grid()
##plt.title("Roll Angle", fontsize="20")
##plt.plot(t_dutch,phi_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(222)
##plt.grid()
##plt.title("Roll Rate", fontsize="20")
##plt.plot(t_dutch,p_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##plt.subplot(212)
##plt.grid()
##plt.title("Yaw Rate", fontsize="20")
##plt.plot(t_dutch,r_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##
###plt.show()
##
###4 spiral
##b , e = list(t).index(3400),list(t).index(3470)
##
##plt.subplot(221)
##plt.grid()
##plt.title("Roll Angle", fontsize="20")
##plt.plot(t_spiral,phi_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Angle [deg]", fontsize="15")
##plt.legend()
##plt.subplot(222)
##plt.grid()
##plt.title("Roll Rate", fontsize="20")
##plt.plot(t_spiral,p_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##plt.subplot(212)
##plt.grid()
##plt.title("Yaw Rate", fontsize="20")
##plt.plot(t_spiral,r_val[b:e],label="Flight Data", color="red")
##plt.xlabel("Flight Time [s]", fontsize="15")
##plt.ylabel("Anglular Speed [deg/s]", fontsize="15")
##plt.legend()
##
###plt.show()

# Start Eigenvalues Calculation Here
#===================================

motion = t_shortperiod
value = q_val

# create desired domain
i_0 = np.where(t == motion[0])
i_end = np.where(t == motion[-1].round(1))
dom = np.arange(int(i_0[0]),int(i_end[0])+1,1)
exact_domain = np.where(DATA[dom,46] == '2.0') 
dom = dom[exact_domain]
motion = motion[exact_domain]

# parameters
V = DATA[dom[0],42].astype(float)
c_mac = 2.0569

value = value[dom]
# identefy local maxima
peaks = np.where(abs(np.hstack((0,value))[:-1]-value) < 0.05) #find indexes of local maxima
av = np.average(value[peaks])
peaks = peaks[0][np.where(value[peaks] > av)]
# create dataset of local maxima
xp = motion[peaks] # xdata
fp = value[peaks]# ydata
a,b,c = np.polyfit(np.log(xp),fp,2) # logarithmic extrapolation of dataset
y = a*np.log(motion)**2 + b*np.log(motion) + c

a0 = y[0]-av
a_half = a0/2 + av
i_half = np.where(abs(y-a_half) == min(abs(y-a_half)))

# T1/2 and P
T_half = motion[i_half]-motion[0]

i_min = np.where(value==min(value))
i_max = np.where(value==max(value))

P = 2*(abs(motion[i_min]-motion[i_max]))

# eigenvalues
eig_r = np.log(0.5)*c_mac/(V*T_half)
eig_c = 2*np.pi*c_mac/(V*P)



print('T1/2: ',T_half,'\nP: ',P,'\nEigenvalue: ',round(eig_r[0],7),' + ',round(eig_c[0],7),'j')

plt.plot(t[dom],y)
plt.plot(t[dom],value)
plt.plot(t[dom],len(value)*[av],'--',color='r')
plt.plot(t[dom],len(value)*[a_half],'--',color='g')
plt.show()









