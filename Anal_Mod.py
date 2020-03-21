# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:03:39 2020

@author: Elliott Desmit
"""

# Citation 550 - Analytical Model
#==============================================================================
#==============================================================================

# Imports
#------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
#==============================================================================

# Stationary flight condition
#------------------------------------------------------------------------------
hp0    = 4000 	       # pressure altitude in the stationary flight condition [m]
V0     = 150           # true airspeed in the stationary flight condition [m/sec]
alpha0 = 2 / 180 * pi  # angle of attack in the stationary flight condition [rad]
th0    = 5 / 180 * pi  # pitch angle in the stationary flight condition [rad]
#==============================================================================

# Aircraft mass
#------------------------------------------------------------------------------
m      = 6000        # mass [kg]
#==============================================================================

# Aerodynamic properties
#------------------------------------------------------------------------------
e      = 0.8         # Oswald factor [ ]
CD0    = 0.04        # Zero lift drag coefficient [ ]
CLa    = 5.084       # Slope of CL-alpha curve [ ]
#==============================================================================

# Longitudinal stability
#------------------------------------------------------------------------------
Cma    = -0.5626     # longitudinal stabilty [ ]
Cmde   = -1.1642     # elevator effectiveness [ ]
#==============================================================================

# Aircraft geometry
#------------------------------------------------------------------------------
S      = 30.00	         # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	         # [ ]
lh     = 0.71 * 5.968    # tail length [m]
c      = 2.0569	         # mean aerodynamic cord [m]
lh_c   = lh / c	         # [ ]
b      = 15.911	         # wing span [m]
bh     = 5.791	         # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	             # [ ]
ih     = -2 * pi / 180   # stabiliser angle of incidence [rad]
#==============================================================================

# Constant values concerning atmosphere and gravity
#------------------------------------------------------------------------------
rho0   = 1.2250          # air density at sea level [kg/m^3] 
lamb   = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)
#==============================================================================

# Air density [kg/m^3]  
#------------------------------------------------------------------------------
rho    = rho0 * pow( ((1+(lamb * hp0 / Temp0))), (-((g / (lamb*R)) + 1)))   
W      = m * g            # [N]       (aircraft weight)
#==============================================================================

# Constant values concerning aircraft inertia
#------------------------------------------------------------------------------
muc    = m / (rho * S * c)
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114
#==============================================================================

# Aerodynamic constants
#------------------------------------------------------------------------------
Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]
#==============================================================================

# Lift and drag coefficient
#------------------------------------------------------------------------------
CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (pi * A * e) # Drag coefficient [ ]
#==============================================================================

# Stabiblity derivatives
#------------------------------------------------------------------------------
CX0    = W * np.sin(th0) / (0.5 * rho * V0 ** 2 * S)
CXu    = -0.09500
CXa    = +0.47966		# Positive! (has been erroneously negative since 1993) 
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -W * np.cos(th0) / (0.5 * rho * V0 ** 2 * S)
CZu    = -0.37616
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939
#==============================================================================

## Characteristic Equation Full Model (probz a mistake, ignore)
##------------------------------------------------------------------------------
#
#A = 8 * muc ** 3 * KY2
#
#b1 = CXu*CZa - 2*muc*CXu - 2*muc*CZa - 2*muc*CZadot
#b2 = 2*muc*Cmq + CZq*Cmadot + 2*muc*Cma - Cmadot*CXu + 2*muc*Cma
#B = 2 * muc * (KY2 * (b1) - (b2))
#
#c1 = CXu*CZa - CXa*CZu
#c2 = CX0*Cmadot + CXu*Cmq + CZa*Cmq + CZadot*Cmq - CXq*Cmu - CZq*Cma + Cma*CXu
#c3 = -CXu*CZadot*Cmq - CZu*Cmadot*CXq + CXq*CZadot*Cmu + CZq*Cmadot*CXu
#C = 2 * muc * (KY2 * (c1) + c2) + c3
#
#d1 = CX0*Cma - CZ0*Cmu - CXa*Cmu
#d2 = CZ0*CZa*Cmu - CZu*Cmadot*CZ0 - CX0*Cmadot*CXu - CXu*CZa*Cmq - CZu*Cma*CXq
#d2 += -CXa*CZq*Cmu + CXq*CZa*Cmu + CXa*CZu*Cmq + CZq*Cma*CXu
#D = 2 * muc * d1 + d2
#
#E = CXa*CX0*Cmu + CZ0*CZa*Cmu - CZu*Cma*CZ0 - CX0*Cma*CXu
#
## get the eigenvalues 
#l1, l2, l3, l4 = np.roots([A,B,C,D,E]) 
#print(l1, l2, l3, l4)
#print()
##==============================================================================

# Characteristic Equation Short Period 
#------------------------------------------------------------------------------

A = 2 * muc * KY2 * (2 * muc - CZadot)

B = - 2 * muc * KY2 * CZa - (2 * muc + CZq) * Cmadot - (2 * muc - CZadot) * Cmq

C = CZa * Cmq - (2 * muc + CZq) * Cma

# get the eigenvalues
l1, l2 = np.roots([A,B,C])
print("Short Period Eigenvalues")
print("Real_____||Complex")
print(round(l1.real,6),"",round(l1.imag,6))
print(round(l2.real,6), round(l2.imag,6))
print()
#==============================================================================

# Characteristic Equation Phugoid
#------------------------------------------------------------------------------

A = 2 * muc * (CZa*Cmq - 2*muc*Cma)

B = 2 * muc * (CXu*Cma - Cmu*CXa) + Cmq * (CZu*CXa - CXu*CZa)

C = CZ0 * (Cmu*CZa - CZu*Cma)

# get the eigenvalues
l1, l2 = np.roots([A,B,C])
print("Phugoid Period Eigenvalues")
print("Real_____||Complex")
print(round(l1.real,6),"",round(l1.imag,6))
print(round(l2.real,6), round(l2.imag,6))
print()
#==============================================================================

# Characteristic Equation Aperiodic Roll
#------------------------------------------------------------------------------

# get the eigenvalues
l1 = Clp / (4 * mub * KX2)
print("Aperiodic Roll Eigenvalue")
print("Real_____||Complex")
print(round(l1.real,6),"",round(l1.imag,6))
print()
#==============================================================================

# Characteristic Equation Dutch Roll
#------------------------------------------------------------------------------

A = 8 * mub **2 * KZ2

B = 2 * mub * (-2 * KZ2 * CYb - Cnr)

C = 4 * mub * Cnb + CYb*Cnr

# get the eigenvalues
l1, l2 = np.roots([A,B,C])
print("Dutch Roll Eigenvalues")
print("Real_____||Complex")
print(round(l1.real,6),"",round(l1.imag,6))
print(round(l2.real,6), round(l2.imag,6))
print()
#==============================================================================

# Characteristic Equation Spiral Motion
#------------------------------------------------------------------------------

# get the eigenvalues
l1 = 2 * CL * (Clb*Cnr - Cnb*Clr) / (Clp * (CYb*Cnr + 4*mub*Cnb) - Cnp * (CYb*Clr + 4*mub*Clb))
print("Spiral Motion Eigenvalue")
print("Real_____||Complex")
print(round(l1.real,6),"",round(l1.imag,6))
print()
#==============================================================================






