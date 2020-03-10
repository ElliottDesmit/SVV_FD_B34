# Citation 550 - Linear simulation
#==============================================================================
#==============================================================================

# Imports
#------------------------------------------------------------------------------
import numpy as np
import control as crtl
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
CXu    = -0.02792
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

# State-space matrices
#------------------------------------------------------------------------------

# Symmetric flight
C1s = np.zeros((4,4)) # matrix for xdot vector

# now store the entries for C1s
c111, c112, c113, c114 = -2*muc, 0, 0, 0
c121, c122, c123, c124 = 0, CZadot - 2*muc, 0, 0
c131, c132, c133, c134 = 0, 0, -1, 0
c141, c142, c143, c144 = 0, Cmadot, 0, -2*muc*KY2

C1s[0,:] = c111, c112, c113, c114
C1s[1,:] = c121, c122, c123, c124
C1s[2,:] = c131, c132, c133, c134
C1s[3,:] = c141, c142, c143, c144
#--

C2s = np.zeros((4,4)) # matrix for x vector

# again store the entries for C2s
c211, c212, c213, c214 = CXu, CXa, CZ0, CXq
c221, c222, c223, c224 = CZu, CZa, -CX0, CZq + 2*muc
c231, c232, c233, c234 = 0, 0, 0, 1
c241, c242, c243, c244 = Cmu, Cma, 0, Cmq

C2s[0,:] = c211, c212, c213, c214
C2s[1,:] = c221, c222, c223, c224
C2s[2,:] = c231, c232, c233, c234
C2s[3,:] = c241, c242, c243, c244
#--

C3s = np.zeros((4,1)) # matrix for u vector

# store the entries for c3s

c311, c321, c331, c341 = CXde, CZde, 0, Cmde

C3s[:,0] = c311, c321, c331, c341
#--

# get the ss matrices
As = np.dot(np.linalg.inv(C1s), -C2s)
Bs = np.dot(np.linalg.inv(C1s), -C3s)
Cs = np.matrix([[0, 1, 0, 0],
                [0, 0, 1, 0]]) # only output alpha and theta
Ds = np.matrix([[0],
                [0]]) # elevator deflection is not an output

sys_s = crtl.ss(As, Bs, Cs, Ds) # symmetric model
#--

# Asymmetric flight
C1a = np.zeros((4,4)) # matrix for xdot vector

c411, c412, c413, c414 = CYbdot - 2*mub, 0, 0, 0
c421, c422, c423, c424 = 0, -1/2, 0, 0
c431, c432, c433, c434 = 0, 0, -4*mub*KX2, 4*mub*KXZ
C441, c442, c443, c444 = Cnbdot, 0, 4*mub*KXZ, -4*mub*KZ2

C1a[0,:] = c411, c412, c413, c414
C1a[1,:] = c421, c422, c423, c424
C1a[2,:] = c431, c432, c433, c434
C1a[3,:] = C441, c442, c443, c444
#--

C2a = np.zeros((4,4)) # matrix for x vector

c511, c512, c513, c514 = CYb, CL, CYp, CYr - 4*mub
c521, c522, c523, c524 = 0, 0, 1, 0
c531, c532, c533, c534 = Clb, 0, Clp, Clr
c541, c542, c543, c544 = Cnb, 0, Cnp, Cnr

C2a[0,:] = c511, c512, c513, c514
C2a[1,:] = c521, c522, c523, c524
C2a[2,:] = c531, c532, c533, c534
C2a[3,:] = c541, c542, c543, c544
#--

C3a = np.zeros((4,2)) # matrix for u vector

c611, c612 = CYda, CYdr
c621, c622 = 0, 0
c631, c632 = Clda, Cldr
c641, c642 = Cnda, Cndr

C3a[0,:] = c611, c612
C3a[1,:] = c621, c622
C3a[2,:] = c631, c632
C3a[3,:] = c641, c642
#--

Aa = np.dot(np.linalg.inv(C1a), -C2a)
Ba = np.dot(np.linalg.inv(C1a), -C3a)
Ca = np.matrix([[1, 0, 0, 0],
                [0, 1, 0, 0]]) # roll and bank angle as output
Da = np.matrix([[0, 0],
                [0, 0]]) # deflections are no outputs

sys_a = crtl.ss(Aa, Ba, Ca, Da)
#==============================================================================

# Plotting the outputs
#------------------------------------------------------------------------------
t = np.arange(0, 5000, 0.1)
t, y1 = crtl.impulse_response(sys_s, t)
t, y2 = crtl.impulse_response(sys_a, t)

plt.subplot(211)
plt.plot(t, 180 * y1[0] / pi, label="angle of attack [deg]")
plt.plot(t, 180 * y1[1] / pi, label="pitch angle [deg]")
plt.legend(), plt.show()

plt.subplot(212)
plt.plot(t, 180 * y2[0] / pi, label="sideslip angle [deg]")
plt.plot(t, 180 * y2[1] / pi, label="bank angle [deg]")
plt.legend(), plt.show()
#==============================================================================
