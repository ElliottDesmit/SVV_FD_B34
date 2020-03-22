# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:43:17 2020

@author: ellio
"""

from Num_Mod import l1s, l2s, l3s, l4s, l1a, l2a, l3a, l4a # numerical eigvals
from Anal_Mod import l1sp, l2sp, l1ph, l2ph, lar, l1dr, l2dr, lsm # analytical eigenvalues

f = open("EV_Comp.txt","w+")

f.write("***Comparison of the eigenvalues from the numerical and analytical model***\n\n")

# short period
f.write("Short Period Eigenvalues\n")
f.write("========================\n")
f.write("Numerical Model\t\t\t|Analytical Model\n")
f.write("Real\t\tComplex\t\t|Real\t\tComplex\n")
f.write(str(round(l1s.real,8))+"\t"+str(round(l1s.imag,8))+"\t|"+str(round(l1sp.real,8))+"\t"+str(round(l1sp.imag,8))+"\n")
f.write(str(round(l2s.real,8))+"\t"+str(round(l2s.imag,8))+"\t|"+str(round(l2sp.real,8))+"\t"+str(round(l2sp.imag,8))+"\n\n")

# phugoid
f.write("Phugoid Eigenvalues\n")
f.write("===================\n")
f.write("Numerical Model\t\t\t|Analytical Model\n")
f.write("Real\t\tComplex\t\t|Real\tComplex\n")
f.write(str(round(l3s.real,8))+"\t"+str(round(l3s.imag,8))+"\t|"+str(round(l1ph.real,8))+"\t"+str(round(l1ph.imag,8))+"\n")
f.write(str(round(l4s.real,8))+"\t"+str(round(l4s.imag,8))+"\t|"+str(round(l2ph.real,8))+"\t"+str(round(l2ph.imag,8))+"\n\n")

# aperiodic roll
f.write("Aperiodic Roll Eigenvalues\n")
f.write("==========================\n")
f.write("Numerical Model\t\t\t|Analytical Model\n")
f.write("Real\t\tComplex\t\t|Real\t\tComplex\n")
f.write(str(round(l1a.real,8))+"\t"+str(round(l1a.imag,8))+"\t\t|"+str(round(lar.real,8))+"\t"+str(round(lar.imag,8))+"\n\n")

# dutch roll
f.write("Dutch Roll Eigenvalues\n")
f.write("======================\n")
f.write("Numerical Model\t\t\t|Analytical Model\n")
f.write("Real\t\tComplex\t\t|Real\t\tComplex\n")
f.write(str(round(l2a.real,8))+"\t"+str(round(l2a.imag,8))+"\t|"+str(round(l1dr.real,8))+"\t"+str(round(l1dr.imag,8))+"\n")
f.write(str(round(l3a.real,8))+"\t"+str(round(l3a.imag,8))+"\t|"+str(round(l2dr.real,8))+"\t"+str(round(l2dr.imag,8))+"\n\n")

f.write("Spiral Motion Eigenvalues\n")
f.write("=========================\n")
f.write("Numerical Model\t\t\t|Analytical Model\n")
f.write("Real\t\tComplex\t\t|Real\t\tComplex\n")
f.write(str(round(l4a.real,8))+"\t"+str(round(l4a.imag,8))+"\t\t|"+str(round(lsm.real,8))+"\t"+str(round(lsm.imag,8)))

f.close()

