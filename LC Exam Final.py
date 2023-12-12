import numpy as np
import pandas as pd
import statistics as st
import math as mt
import time
from scipy.stats import norm

# Default values subject to change
start = time.time()
def_P = 1000000
def_m = .003
def_r = .05
def_sigma = .2
def_x = 60
def_St = .9995
disc = 1.1



def Makeham(s, x, A=.0001, B=.00035, c=1.075):
    return np.exp(-A*s - B/np.log(c)*mt.pow(c, x)*(pow(c, s) - 1))

def pi(time=0):

    pi_in=0
    upsilon = 0
    psi = 0
    adj_St = def_St**time
    
    def v(t, s, St=adj_St, m=def_m, r=def_r, sigma=def_sigma):
        d1 = (np.log(St*pow(1-m, 12*s)) + (r + pow(sigma, 2)/2)*(s-t)) / (sigma*mt.sqrt(s-t))
        d2 = d1 - sigma*mt.sqrt(s-t)
        left = np.exp(-r*(s-t))*norm.cdf(-d2) 
        right = -St*pow(1-m, 12*s)*norm.cdf(-d1)
        return (left, right)
    
    for i in range(time+1,61):
        upsilon += v(t=time/12, s=i/12)[0] * (Makeham(s=(i-1-time)/12, x=def_x+time/12) - Makeham(s=(i-time)/12, x=def_x+time/12))
        psi += v(t=time/12, s=i/12)[1] * (Makeham(s=(i-1-time)/12, x=def_x+time/12) - Makeham(s=(i-time)/12, x=def_x+time/12))
        pi_in += (v(t=time/12, s=i/12)[0] + v(t=time/12, s=i/12)[1]) * (Makeham(s=(i-1-time)/12, x=def_x+time/12) - Makeham(s=(i-time)/12, x=def_x+time/12))
  
    upsilon += v(t=time/12, s=60/12)[0] * Makeham(s=(60-time)/12, x=def_x+time/12)
    psi += v(t=time/12, s=60/12)[1] * Makeham(s=(60-time)/12, x=def_x+time/12)
    pi_in += (v(t=time/12, s=60/12)[0] + v(t=time/12, s=60/12)[1]) * Makeham(s=(60-time)/12, x=def_x+time/12)

    return (pi_in, upsilon, psi)


Ft = []
MC = []
expenses = []
for i in range(0,60):
    ft = def_P*pow(def_St, i)*pow(1-def_m, i)
    Ft.append(round(ft, 2))
    MC.append(round(ft*def_m, 2))
    expenses.append(round(def_P*pow(def_St,i)*pow((1-def_m), i+1)*.00025, 2))

guarantee = [0]
COH = [112709.54]
for h in range(1,60):
    COH.append(round(def_P*(pi(time=h)[0]*Makeham(s=1/12, x=def_x+(h-1)/12) - pi(time=h-1)[1]*np.exp(def_r/12) - pi(time=h-1)[2]*def_St), 2))
    guarantee.append(round((1-Makeham(s=1/12, x=def_x+(h-1)/12))*max(0, def_P-Ft[h]), 2))

Pr = []
for j in range(0,60):
    profit = MC[j] - expenses[j] - guarantee[j] - COH[j]
    if j > 1:
        profit = profit*Makeham(s=1/12, x=def_x+(j-1)/12)*pow(disc, -j/12)
    Pr.append(round(profit, 2))

Overall = pd.DataFrame({"Fund": Ft, "Manage Charges": MC, "Expenses": expenses, 
                        "guarantee": guarantee, "Cost of Hedge": COH, "Profit": Pr})
print(Overall)
print(f"The NPV of the Portfolios is {sum(Pr)}.")
print(f"Completed in {round(time.time() - start, 2)} seconds.")
