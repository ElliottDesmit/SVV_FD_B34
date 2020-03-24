from numpy import *
from Flight_Data import DATA
from matplotlib import pyplot as plt

#=======================================================================================

# USER INPUT

x_ax = 48

# choose desired measurements (see below)

# subplot 1
y_ax = 16
y_ax2 = 26

#subplot 2
y_ax3 = 18
y_ax4 = 28


aper_roll = [2695,2775,'Aperiodic Roll','A'] 
short_period = [2755,2850,'Short Period Motion','S']
dutch_roll = [2850,2900,'Dutch Roll','A']
dutch_roll_yd = [2910,2970, 'Dutch Roll YD','A']
phugoid = [2970,3180,'Phugoid','S']
spiral = [3250,3350,'Spiral','A']
zero_g = [3500,3550,'Zero G','']
full = [9,4564,'full flight','']

custom = [2650,3600,'custom timeframe',''] 

motion = dutch_roll # choose motion

#=======================================================================================

# DERIVE EIGENVALUES FROM DATA

i_0 = where(DATA[2:,48].astype(float) == motion[0])
i_end = where(DATA[2:,48].astype(float) == motion[1])
dom = arange(int(i_0[0])+2,int(i_end[0])+3,1) # create desired domain

exact_domain = where(DATA[dom,46] != '0.0')
indexes = dom[exact_domain]

if motion[3] == 'A':

    bèta = DATA[indexes,49].astype(float)
    phi = DATA[indexes,21].astype(float)
    p = DATA[indexes,26].astype(float)
    r = DATA[indexes,28].astype(float)
    x = array([bèta,phi,p,r])

    d_e = DATA[indexes,16].astype(float)
    d_r = DATA[indexes,18].astype(float)
    u = array([d_e,d_r])

    x_dot = array([0,0,0,0])
    for i in range(1,len(indexes-1)):
        xdot = (x[:,i]-x[:,i-1])/0.1
        x_dot = vstack((x_dot,xdot))
    x_dot = x_dot.T    
    
        
dom = indexes

#=======================================================================================

# PROGRAM PLOTS


col1 ='r' # color for y axis 1
col2 ='b' # color for y axis 2

fig, (ax1,ax3) = plt.subplots(2,1,sharex=True)

#subplot 1
ax1.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax].astype(float),color=col1)
ax1.set_xlabel(DATA[0,x_ax]+' ['+DATA[1,x_ax]+']')
ax1.set_ylabel(DATA[0,y_ax]+' ['+DATA[1,y_ax]+']',color=col1)
ax1.tick_params(axis='y', labelcolor=col1)

ax2 = ax1.twinx()

ax2.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax2].astype(float),color=col2)
ax2.set_ylabel(DATA[0,y_ax2]+' ['+DATA[1,y_ax2]+']',color=col2)
ax2.tick_params(axis='y', labelcolor=col2)

plt.title(DATA[0,y_ax]+' & '+DATA[0,y_ax2]+' over '+DATA[0,x_ax]+'\nfor '+motion[2])

#subplot 2
ax3.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax3].astype(float),color=col1)
ax3.set_xlabel(DATA[0,x_ax]+' ['+DATA[1,x_ax]+']')
ax3.set_ylabel(DATA[0,y_ax3]+' ['+DATA[1,y_ax3]+']',color=col1)
ax3.tick_params(axis='y', labelcolor=col1)

ax4 = ax3.twinx()

ax4.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax4].astype(float),color=col2)
ax4.set_ylabel(DATA[0,y_ax4]+' ['+DATA[1,y_ax4]+']',color=col2)
ax4.tick_params(axis='y', labelcolor=col2)

plt.title(DATA[0,y_ax3]+' & '+DATA[0,y_ax4]+' over '+DATA[0,x_ax]+'\nfor '+motion[2])

fig.tight_layout()

plt.show()

""" DATA[:,i] with i :

    0='Angle of attack'
    1='Deflection of elevator trim'
    2='Force on elevator control wheel'
    3='Engine 1: Fuel mass flow'
    4='Engine 2: Fuel mass flow'
    5='Engine 1: Inter Turbine Temperature (ITT)'
    6='Engine 2: Inter turbine temperature (ITT)'
    7='Engine 1: Oil pressure'
    8='Engine 2: Oil pressure'
    9='Deflection of the control column (Se or DCOC)',
    10='Engine 1: Fan speed (N1)'
    11='Engine 1: Turbine speed (N2)'
    12='Engine 2: Fan speed (N1)'
    13='Engine 2: Turbine speed (N2)'
    14='calculated fuel used by fuel mass flow'
    15='calculated fuel used by fuel mass flow'
    16='Deflection of aileron (right wing?)'
    17='Deflection of elevator'
    18='Deflection of rudder'
    19='UTC Date DD:MM:YY'
    20='UTC Seconds'
    21='Roll Angle'
    22='Pitch Angle'
    23='<no description>'
    24='GNSS Latitude'
    25='GNSS Longitude'
    26='Body Roll Rate'
    27='Body Pitch Rate'
    28='Body Yaw Rate'
    29='Body Long Accel'
    30='Body Lat Accel'
    31='Body Norm Accel'
    32='Along Heading Accel'
    33='Cross Heading Accel'
    34='Vertical Accel'
    35='Static Air Temperature'
    36='Total Air Temperature'
    37='Pressure Altitude (1013.25 mB)'
    38='Baro Corrected Altitude n1'
    39='no descr'
    40='Mach'
    41='Computed Airspeed'
    42='True Airspeed'
    43='Altitude Rate'
    44='Measurement Running'
    45='Number of Measurements Ready'
    46='Status of graph'
    47='Active Screen'
    48='Time'
    49 = sideslip angle  (calculated arctan('33'/'32') ) """
