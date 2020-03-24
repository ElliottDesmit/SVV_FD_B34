# Imports

import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from Num_Mod import num_mod
from Valid_ED import u_val, alpha_val, theta_val, q_val, delta_a, delta_r, delta_e, phi_val, p_val, r_val, t, height, V_0, m_t



# times

t_aperiodic = np.arange(2711,2750,0.1)
input_ap_a = delta_a[list(t).index(2711):list(t).index(2750)]
input_ap_r = delta_r[list(t).index(2711):list(t).index(2750)]
input_ap = np.vstack((input_ap_a,input_ap_r))

t_shortperiod = np.arange(2766,2770,0.1)
input_short = delta_e[list(t).index(2766):list(t).index(2770)]


t_dutch = np.arange(2850,2880,0.1)
input_dutch_a = delta_a[list(t).index(2850):list(t).index(2880)]
input_dutch_r = delta_r[list(t).index(2850):list(t).index(2880)]
input_dutch = np.vstack((input_dutch_a,input_dutch_r))

t_yaw = np.arange(2850,2880,0.1)
input_yaw_a = delta_a[list(t).index(2850):list(t).index(2880)]
input_yaw_r = delta_r[list(t).index(2850):list(t).index(2880)]
input_yaw = np.vstack((input_yaw_a,input_yaw_r))


t_phugoid = np.arange(2975,3128,0.1)
input_phugoid = delta_e[list(t).index(2975):list(t).index(3128)]


t_spiral = np.arange(3400,3470,0.1)
input_spiral_a = delta_a[list(t).index(3400):list(t).index(3470)]
input_spiral_r = delta_r[list(t).index(3400):list(t).index(3470)]
input_spiral = np.vstack((input_spiral_a,input_spiral_r))

# Symmetric

#1 Short period

b , e = list(t).index(2766) , list(t).index(2770)
sys_s ,_,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x1 = ctrl.forced_response(sys_s, t_shortperiod,input_short)

#plt.subplot(221)
#plt.title("Deviation from Nominal Speed")
#plt.plot(t1,sim_s1[0]+np.ones(len(t1))*u_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,u_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Speed [m/s]")
#plt.legend()
#plt.subplot(222)
#plt.title("Angle of Attack")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*alpha_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,alpha_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(223)
#plt.title("Pitch Angle")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*theta_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,theta_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(224)
#plt.title("Pitch rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*q_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,q_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angular Speed [deg/s]")
#plt.legend()
#
#plt.show()


#2 Phugoid
b , e = list(t).index(2975) , list(t).index(3128)
sys_s ,_,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_s, t_phugoid, input_phugoid)

#plt.subplot(221)
#plt.title("Deviation from Nominal Speed")
#plt.plot(t1,sim_s1[0]+np.ones(len(t1))*u_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,u_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Speed [m/s]")
#plt.legend()
#plt.subplot(222)
#plt.title("Angle of Attack")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*alpha_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,alpha_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(223)
#plt.title("Pitch Angle")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*theta_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,theta_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(224)
#plt.title("Pitch Rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*q_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,q_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angular Speed [deg/s]")
#plt.legend()
#
#plt.show()

#Asymmetric
#1 Aperiodic
b , e = list(t).index(2711) , list(t).index(2750)
_ ,sys_a,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_aperiodic, input_ap)

#plt.subplot(221)
#plt.title("Roll Angle")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*phi_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,phi_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(222)
#plt.title("Roll Rate")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*p_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,p_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#plt.subplot(212)
#plt.title("Yaw Rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*r_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,r_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#
#plt.show()

#2 dutch
b , e = list(t).index(2850),list(t).index(2880)
_ ,sys_a,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_dutch, input_dutch)

#plt.subplot(221)
#plt.title("Roll Angle")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*phi_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,phi_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(222)
#plt.title("Roll Rate")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*p_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,p_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#plt.subplot(212)
#plt.title("Yaw Rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*r_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,r_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#
#plt.show()

#3 dutch roll yaw damper
b , e = list(t).index(2850),list(t).index(2880)
_ ,sys_a,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_yaw, input_yaw)

#plt.subplot(221)
#plt.title("Roll Angle")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*phi_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,phi_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(222)
#plt.title("Roll Rate")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*p_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,p_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#plt.subplot(212)
#plt.title("Yaw Rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*r_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,r_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#
#plt.show()

#4 spiral
b , e = list(t).index(3400),list(t).index(3470)
_ ,sys_a,_,_,_,_,_,_,_,_= num_mod(height[b],V_0[b],m_t[b])
t1, sim_s1, x2 = ctrl.forced_response(sys_a, t_spiral, input_spiral)

#plt.subplot(221)
#plt.title("Roll Angle")
#plt.plot(t1,sim_s1[1] * 180 / np.pi+np.ones(len(t1))*phi_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,phi_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Angle [deg]")
#plt.legend()
#plt.subplot(222)
#plt.title("Roll Rate")
#plt.plot(t1,sim_s1[2] * 180 / np.pi+np.ones(len(t1))*p_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,p_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#plt.subplot(212)
#plt.title("Yaw Rate")
#plt.plot(t1,sim_s1[3] * 180 / np.pi+np.ones(len(t1))*r_val[b:e][0],label="Simulated Data", color="blue")
#plt.plot(t1,r_val[b:e],label="Flight Data", color="red")
#plt.xlabel("Flight Time [s]")
#plt.ylabel("Anglular Speed [deg/s]")
#plt.legend()
#
#plt.show()


