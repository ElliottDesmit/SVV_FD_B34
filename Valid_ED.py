# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:43:14 2020

@author: Elliott Desmit
"""

# imports
from Fligth_Data import DATA
import control as ctrl
from Num_Mod import num_mod
import numpy as np
from Mass_cg import M_t_DATA
import matplotlib.pyplot as plt

alpha0 = 1.4 / 180 * np.pi
th0 = alpha0

# function to fix the mess
def fixit(arr) :
    arr_n = np.zeros(arr.shape)
    for i in range(arr.shape[0]):
        arr_n[i] = float(arr[i])
    return arr_n    

# creating all relevant arrays
t = fixit(DATA[2:,48]) # time array

# symm
delta_e = np.pi * fixit(DATA[2:,17]) / 180 # elevator input [rad]

u_val = fixit(DATA[2:,41]) - fixit(DATA[2:,42]) # speed deviation experimental [m/s]
alpha_val = fixit(DATA[2:,0]) - (180 * alpha0 / np.pi) # AoA experimental [deg]
theta_val = fixit(DATA[2:,22]) - (180 * th0 / np.pi) # th experimental [deg]
q_val = fixit(DATA[2:,27]) # q experimental [deg/s]



# asymm
delta_a = np.pi * fixit(DATA[2:,16]) / 180 # aileron input [rad]
delta_r = np.pi * fixit(DATA[2:,18]) / 180 # rudder input [rad]
delta_in = np.vstack((delta_a,delta_r))

#beta_val = fixit(DATA[:,?]) # side slip angle experimental [deg]
phi_val = fixit(DATA[2:,21]) # `roll angle experimental [deg]
p_val = fixit(DATA[2:,26]) # roll rate experimental [deg/s]
r_val = fixit(DATA[2:,28]) # yaw rate experimental [deg/s]


#num mod values

height = fixit(DATA[2:,37])
V_0 = fixit(DATA[2:,42])
m_t = M_t_DATA

# t, sim_a, x = ctrl.forced_response(sys_a, t, delta_in)
#t, sim_s, x = ctrl.forced_response(sys_s, t, delta_e) # u, AoA, th, q simulated
# # Symmetric Parameters
# #------------------------------------------------------------------------------
#
# #plotting u vs time
# plt.subplot(221)
# plt.plot(t, sim_s[0], label="Simulated Data")
# plt.plot(t, u_val, label="Flight Data")
# plt.xlabel("Flight Time [s]")
# plt.ylabel("Speed Deviation [m/s]")
#
# # plotting alpha vs time
# plt.subplot(222)
# plt.plot(t, (180 * sim_s[1] / np.pi), label="Simulation Data")
# plt.plot(t, alpha_val, label="Flight Data")
# plt.xlabel("Flight Time [s]")
# plt.ylabel("Angle of Attack [deg]")
#
# # plotting theta vs time
# plt.subplot(223)
# plt.plot(t, (180 * sim_s[2] / np.pi), label="Simulation Data")
# plt.plot(t, theta_val, label="Flight Data")
# plt.xlabel("Flight Time [s]")
# plt.ylabel("Pitch Angle [deg]")
#
# # plotting q vs time
# plt.subplot(224)
# plt.plot(t, (180 * sim_s[3] / np.pi), label="Simulated Data")
# plt.plot(t, q_val, label="Flight Data")
# plt.xlabel("Flight Time [s]")
# plt.ylabel("Pitch Rate [deg/s]")
# plt.legend(), plt.show()
#==============================================================================

# Asymmetric Parameters
#------------------------------------------------------------------------------

##plotting beta vs time
#plt.subplot(221)
#plt.plot(t, sim_a[0], label="Simulated Data")
#plt.plot(t, beta_val, label="Flight Data")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle of Side Slip [m/s]")

# plotting phi vs time
#plt.subplot(311)
#plt.plot(t, (180 * sim_a[1] / np.pi), label="Simulation Data")
#plt.plot(t, phi_val, label="Flight Data")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Roll Angle [deg]")
#
## plotting p vs time
#plt.subplot(312)
#plt.plot(t, (180 * sim_a[2] / np.pi), label="Simulation Data")
#plt.plot(t, p_val, label="Flight Data")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Roll Rate [deg/s]")
#
## plotting r vs time
#plt.subplot(313)
#plt.plot(t, (180 * sim_a[3] / np.pi), label="Simulated Data")
#plt.plot(t, r_val, label="Flight Data")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Yaw Rate [deg/s]")
#plt.legend(), plt.show()