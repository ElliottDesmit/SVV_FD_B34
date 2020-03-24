from numpy import *

""" Creates an array 'DATA' with all measurements in columns.
    1st and 2nd row contain description adn units.
    For list of indexes and corresponding data, see below.
    Note: values are type 'string'. """


# CREATE DATA ARRAY


V = genfromtxt('data_ref.txt',skip_header=2,delimiter=',',dtype=float,comments='$')
D = genfromtxt('data_ref.txt', skip_header=0, max_rows=1,delimiter=',',dtype=str,comments='$')
#U = genfromtxt('data.txt', skip_header=1, max_rows=1,delimiter=',',dtype=str,comments='$')


#Dat = vstack((U,V))
#Dat = vstack((D,Dat))

# CONVERT UNITS

conv_fac = array([1,1,1,\
                  0.45359/(60*60),\
                  0.45359/(60*60),\
                  1,1,\
                  0.0068948,\
                  0.0068948,\
                  #1,
                  1,1,1,1,\
                  0.45359,\
                  0.45359,\
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
                  0.3048,\
                  0.3048,\
                  1,1,\
                  0.51444,\
                  0.51444,\
                  0.3048/60,\
                  1,1,1,1,1])

C = V*conv_fac

SIU = array(['deg','deg','N','kg/s','kg/s','°C','°C','N/mm²','N/mm²',#'deg',\
             '%','%','%','%','kg','kg',\
             'deg','deg','deg','DD:MM:YY','sec','deg','deg','/','deg','deg','deg/s','deg/s','deg/s',\
             'g', 'g', 'g', 'g', 'g', 'g','°C','°C','m','m','/','Mach','m/s','m/s','m/s','/','/','/','/','sec'])

DATA = vstack((D,SIU))
DATA = hstack((DATA.T,C.T))
DATA = DATA.T

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
