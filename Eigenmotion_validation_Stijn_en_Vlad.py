# Imports

import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from Num_Mod import num_mod
from Valid_ED import u_val, alpha_val, theta_val, q_val, delta_a, delta_r, delta_in, delta_e,phi_val, p_val, r_val, t, height,V_0,m_t



# times

t_aperiodic = np.arange(2708,2768,0.1)
input_ap_a = delta_a[list(t).index(2708):list(t).index(2768)]
input_ap_r = delta_r[list(t).index(2708):list(t).index(2768)]
input_ap = np.vstack((input_ap_a,input_ap_r))

t_shortperiod = np.arange(2768,2828,0.1)
input_short = delta_e[list(t).index(2768):list(t).index(2828)]


t_dutch = np.arange(2828,2888,0.1)
input_dutch_a = delta_a[list(t).index(2828):list(t).index(2888)]
input_dutch_r = delta_r[list(t).index(2828):list(t).index(2888)]
input_dutch = np.vstack((input_dutch_a,input_dutch_r))

t_yaw = np.arange(2888,2948,0.1)
input_yaw_a = delta_a[list(t).index(2888):list(t).index(2948)]
input_yaw_r = delta_r[list(t).index(2888):list(t).index(2948)]
input_yaw = np.vstack((input_yaw_a,input_yaw_r))


t_phugoid = np.arange(2948,3248,0.1)
input_phugoid = delta_e[list(t).index(2948):list(t).index(3248)]


t_spiral = np.arange(3248,3548,0.1)
input_spiral_a = delta_a[list(t).index(3248):list(t).index(3548)]
input_spiral_r = delta_r[list(t).index(3248):list(t).index(3548)]
input_spiral = np.vstack((input_spiral_a,input_spiral_r))

# Symmetric

#1 Short period

b , e = list(t).index(2768) , list(t).index(2828)
sys_s ,_,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x1 = ctrl.forced_response(sys_s, t_shortperiod,input_short)

plt.subplot(221)
plt.plot(t1,sim_s1[0],label="Deviation from nom speed")
plt.plot(t1,u_val[b:e]-np.ones(len(t1))*u_val[b:e][0],label="Data")
plt.legend()
plt.title("Short period")
plt.subplot(222)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="Angle of attack")
plt.plot(t1,alpha_val[b:e]-np.ones(len(t1))*alpha_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="Pitch angle")
plt.plot(t1,theta_val[b:e]-np.ones(len(t1))*theta_val[b:e][0],label="Data")
plt.legend()
plt.subplot(224)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="pitch rate")
plt.plot(t1,q_val[b:e]-np.ones(len(t1))*q_val[b:e][0],label="Data")
plt.legend()

plt.show()


#2 Phugoid
b , e = list(t).index(2948) , list(t).index(3248)
sys_s ,_,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_s, t_phugoid, input_phugoid)

plt.subplot(221)
plt.plot(t1,sim_s1[0],label="Deviation from nom speed")
plt.plot(t1,u_val[b:e]-np.ones(len(t1))*u_val[b:e][0],label="Data")
plt.legend()
plt.title("Phugoid")
plt.subplot(222)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="Angle of attack")
plt.plot(t1,alpha_val[b:e]-np.ones(len(t1))*alpha_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="Pitch angle")
plt.plot(t1,theta_val[b:e]-np.ones(len(t1))*theta_val[b:e][0],label="Data")
plt.legend()
plt.subplot(224)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="pitch rate")
plt.plot(t1,q_val[b:e]-np.ones(len(t1))*q_val[b:e][0],label="Data")
plt.legend()

plt.show()

#Asymmetric
#1 Aperiodic
b , e = list(t).index(2708) , list(t).index(2768)
_ ,sys_a,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_aperiodic, input_ap)

plt.subplot(221)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="phi")
plt.plot(t1,phi_val[b:e]-np.ones(len(t1))*phi_val[b:e][0],label="Data")
plt.legend()
plt.title("Aperiodic")
plt.subplot(222)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="p")
plt.plot(t1,p_val[b:e]-np.ones(len(t1))*p_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="r")
plt.plot(t1,r_val[b:e]-np.ones(len(t1))*r_val[b:e][0],label="Data")
plt.legend()


plt.show()

#2 dutch
b , e = list(t).index(2828),list(t).index(2888)
_ ,sys_a,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_dutch, input_dutch)

plt.subplot(221)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="phi")
plt.plot(t1,phi_val[b:e]-np.ones(len(t1))*phi_val[b:e][0],label="Data")
plt.legend()
plt.title("Dutch")
plt.subplot(222)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="p")
plt.plot(t1,p_val[b:e]-np.ones(len(t1))*p_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="r")
plt.plot(t1,r_val[b:e]-np.ones(len(t1))*r_val[b:e][0],label="Data")
plt.legend()


plt.show()

#3 yaw
b , e = list(t).index(2888),list(t).index(2948)
_ ,sys_a,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_yaw, input_yaw)

plt.subplot(221)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="phi")
plt.plot(t1,phi_val[b:e]-np.ones(len(t1))*phi_val[b:e][0],label="Data")
plt.legend()
plt.title("Dutch yaw")
plt.subplot(222)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="p")
plt.plot(t1,p_val[b:e]-np.ones(len(t1))*p_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="r")
plt.plot(t1,r_val[b:e]-np.ones(len(t1))*r_val[b:e][0],label="Data")
plt.legend()


plt.show()

#4 spiral
b , e = list(t).index(3248),list(t).index(3548)
_ ,sys_a,_,_= num_mod(height[b],V_0[b],m_t[b],alpha_val[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_spiral, input_spiral)

plt.subplot(221)
plt.plot(t1,sim_s1[1] * 180 / np.pi,label="phi")
plt.plot(t1,phi_val[b:e]-np.ones(len(t1))*phi_val[b:e][0],label="Data")
plt.legend()
plt.title("Spiral")
plt.subplot(222)
plt.plot(t1,sim_s1[2] * 180 / np.pi,label="p")
plt.plot(t1,p_val[b:e]-np.ones(len(t1))*p_val[b:e][0],label="Data")
plt.legend()
plt.subplot(223)
plt.plot(t1,sim_s1[3] * 180 / np.pi,label="r")
plt.plot(t1,r_val[b:e]-np.ones(len(t1))*r_val[b:e][0],label="Data")
plt.legend()


plt.show()


