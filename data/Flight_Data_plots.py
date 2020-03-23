from numpy import *
from Flight_Data import DATA
from matplotlib import pyplot as plt

x_ax = 48 

y_ax = 17 # choose desired measurements
y_ax2 = 22

aper_roll = [arange(2690,2770.1,0.1),'Aperiodic Roll']
short_period = [arange(2750,2830.1,0.1),'Short Period Motion']
dutch_roll = [arange(2810,2890.1,0.1),'Dutch Roll']
dutch_roll_yd = [arange(2870,2950.1,0.1), 'Dutch Roll YD']
phugoid = [arange(2930,3250.1,0.1),'Phugoid']#when does phugoid motion end?
spiral = [arange(3230,3360.1,0.1),'Spiral']#when does spiral motion end?

motion = phugoid # choose motion

##t_start = 2690 # time measurements start at 9.0 sec
##t_stop = 2770 #time measurements end at 4564.0 sec
##
##i_0 = where(DATA[2:,48].astype(float)==t_start)
##i_end = where(DATA[2:,48].astype(float)==t_stop)
##dom = arange(int(i_0[0])+2,int(i_end[0])+3,1) # create desired domain
dom = (motion[0]*10).astype(int)

col1 ='r' # color for y axis 1
col2 ='b' # color for y axis 2

fig, ax1 = plt.subplots()

ax1.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax].astype(float),color=col1)
ax1.set_xlabel(DATA[0,x_ax]+' ['+DATA[1,x_ax]+']')
ax1.set_ylabel(DATA[0,y_ax]+' ['+DATA[1,y_ax]+']',color=col1)
ax1.tick_params(axis='y', labelcolor=col1)

ax2 = ax1.twinx()

ax2.plot(DATA[dom,x_ax].astype(float),DATA[dom,y_ax2].astype(float),color=col2)
ax2.set_ylabel(DATA[0,y_ax2]+' ['+DATA[1,y_ax2]+']',color=col2)
ax2.tick_params(axis='y', labelcolor=col2)

plt.title(DATA[0,y_ax]+' & '+DATA[0,y_ax2]+' vs. '+DATA[0,x_ax]+'\nfor '+motion[1])

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
    48='Time' """
