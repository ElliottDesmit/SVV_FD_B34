from numpy import *

# CREATE DATA ARRAY

file = open('readme.txt','r')
data = file.readlines()

V = genfromtxt('data.txt',skip_header=2,delimiter=',')
D = genfromtxt(data, skip_header=0, max_rows=1,delimiter=',',dtype=str)
U = genfromtxt(data, skip_header=1, max_rows=1,delimiter=',',dtype=str)

file.close()

Dat = vstack((U,V))
Dat = vstack((D,Dat))

# CONVERT DATA

conv_fac = array([1,1,1,\
                  0.45359/(60*60),\
                  0.45359/(60*60),\
                  1,1,\
                  0.0068948,\
                  0.0068948,\
                  1,1,1,1,1,\
                  0.45359,\
                  0.45359,\
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
                  0.3048,\
                  0.3048,\
                  1,1,\
                  0.51444,\
                  0.51444,\
                  0.3048/60,\
                  1,1,1,1])

C = V*conv_fac

SIU = array(['deg','deg','N','kg/s','kg/s','°C','°C','N/mm²','N/mm²','deg','%','%','%','%','kg','kg',\
             'deg','deg','deg','DD:MM:YY','s','deg','deg','/','deg','deg','deg/s','deg/s','deg/s',\
             'g', 'g', 'g', 'g', 'g', 'g','°C','°C','m','m','/','Mach','m/s','m/s','m/s','/','/','/','/'])

DATA = vstack((SIU,C))
DATA = vstack((D,DATA))

