import numpy as np
import pandas as pd
import statistics as st
import math as mt
import time


start = time.time()
def_n=10
def_i=.09
def_mcr=.0075
def_e0 = .05
def_e = .01
def_p = 5500
def_q = .005
def_r = .15
def_r_mean = .074928
def_r_sd = .15
def_gmmb = def_n*def_p

def monte_carlo(n, mcr, e0, e, p, q, r, r_mean, r_sd, gmmb):
    # Simulate random intrest rates
    sim_r=[]
    for s in range(0,n+1) :
        sim_r.append(np.random.lognormal(r_mean, r_sd))

    sim_rt = pd.DataFrame(data={"sim_rt": sim_r})
    # print(sim_rt)

    # Constant interest
    # inc = 1+i
    # inc0 = inc

    # Variable interest
    inc0 = sim_r[0]

    # Table 15.1 using constant or random interest rates
    start = {"t": [1], "APt": [(1-e0)*p], "F(t-1)": [0], "Ft-": [(1-e0)*p*inc0], "MCt": [mcr*(0+(1-e0)*p)*inc0], "Ft": [(1-mcr)*((1-e0)*p)*inc0]}
    table_151 = pd.DataFrame(data=start)
    for s in range(1,n):
        next = {"t": [1+s], "APt": [(1-e)*p], "F(t-1)": [table_151.at[s-1, "Ft"]], "Ft-": [((1-e)*p+table_151.at[s-1, "Ft"])*sim_r[s]]
                , "MCt": [mcr*(table_151.at[s-1, "Ft"]+(1-e)*p)*sim_r[s]], "Ft": [(1-mcr)*(table_151.at[s-1, "Ft"]+(1-e)*p)*sim_r[s]]}
        table_151 = pd.concat([table_151, pd.DataFrame(next)], ignore_index=True)
    # Add a t=0 row
    table_151 = pd.concat([pd.DataFrame({"t": [0], "APt": [0], "F(t-1)": [0], "Ft-": [0], "MCt": [0], "Ft": [0]}), table_151], ignore_index=True)

    # Include  variables from table 15.2
    extra = pd.DataFrame({"UAPt": [0]+list(p-table_151.loc[1:10,"APt"]), "Et": list((.1*p+150, 0))+[.005*p for s in range(1,10)]
                          , "EDBt": list(.005*.1*table_151.loc[:,"Ft"])})
    extra2 = pd.DataFrame(data={"It": [0]+list(.06*(extra.loc[1:10,"UAPt"]-extra.loc[1:10,"Et"]))})
    extra3 = pd.DataFrame(data={"Prt": list(extra.loc[:,"UAPt"]-extra.loc[:,"Et"]+extra2.loc[:,"It"]+table_151.loc[:,"MCt"]-extra.loc[:,"EDBt"])})
    extra3.at[10,"Prt"] = (extra3.at[10,"Prt"] - (1-q)*max(gmmb-table_151.at[10,"Ft"],0))

    # Include variables from table 15.3
    pif=pd.DataFrame(data={"PIF": [1]+[1]+[pow(1-q,1)*.9]+[pow(1-q,2)*.9*.95]
                              +[pow(1-q,t)*.9*.95 for t in range(3,10)]})
    extra4=pd.DataFrame(data={"Πt": list(extra3.loc[:,"Prt"]*pif.loc[:,"PIF"])})

    # Combination of table 15.1, 15.2, and 15.3
    table_agg = table_151.join(extra).join(extra2).join(extra3).join(extra4).join(sim_rt)
    # print(table_agg)
    # print(table_agg[["sim_rt", "MCt", "Ft", "Prt", "Πt"]])

    # Calculate the GMMB if it is < $50,000
    GMMB = (1-q)*max(gmmb-table_agg.at[10,"Ft"],0)
    # print(f"GMMB: {GMMB}.")

    # Calculate the NPV
    # NPV = print(f"NPV: {sum([table_agg.at[t, 'Πt']*pow(1+r,-t) for t in range(0,11)])}.")
    NPV = sum([table_agg.at[t, 'Πt']*pow(1+r,-t) for t in range(0,11)])
    return (NPV, GMMB)


def table_158(NPVs, GMMB):
    return pd.DataFrame(data=[st.mean(NPVs), np.std(NPVs)
                        , (round(st.mean(NPVs)-1.96*st.stdev(NPVs)/mt.sqrt(sim), 2), round(st.mean(NPVs)+1.96*st.stdev(NPVs)/mt.sqrt(sim), 2))
                        , np.percentile(NPVs, 5), st.median(NPVs), np.percentile(NPVs, 95), sum([NPVs[t]<0 for t in range(0,sim)])
                        , sum([GMMB[t]==0 for t in range(0,sim)])]
                        
                        , columns= [""])
    
# Simulate many policies
sim = 1000

NPVs0 = []
for s in range(0,sim):
    temp = monte_carlo(n=def_n, mcr=def_mcr, e0=def_e0, e=def_e, p=def_p, q=def_q, r=def_r, r_mean=def_r_mean, r_sd=def_r_sd, gmmb=def_gmmb)
    NPVs0.append(temp)
table_159_def = list(table_158([NPVs0[t][0] for t in range(0,sim)], [NPVs0[t][1] for t in range(0,sim)]).loc[:,""])

NPVs0 = []
for s in range(0,sim):
    temp = monte_carlo(n=def_n, mcr=def_mcr, e0=def_e0, e=def_e, p=5500, q=def_q, r=def_r, r_mean=def_r_mean, r_sd=def_r_sd, gmmb=def_gmmb)
    NPVs0.append(temp)
table_159_P = list(table_158([NPVs0[t][0] for t in range(0,sim)], [NPVs0[t][1] for t in range(0,sim)]).loc[:,""])

NPVs0 = []
for s in range(0,sim):
    temp = monte_carlo(n=def_n, mcr=.0125, e0=def_e0, e=def_e, p=def_p, q=def_q, r=def_r, r_mean=def_r_mean, r_sd=def_r_sd, gmmb=def_gmmb)
    NPVs0.append(temp)
table_159_MC = list(table_158([NPVs0[t][0] for t in range(0,sim)], [NPVs0[t][1] for t in range(0,sim)]).loc[:,""])

NPVs0 = []
for s in range(0,sim):
    temp = monte_carlo(n=def_n, mcr=def_mcr, e0=.06, e=.02, p=def_p, q=def_q, r=def_r, r_mean=def_r_mean, r_sd=def_r_sd, gmmb=def_gmmb)
    NPVs0.append(temp)
table_159_UAP = list(table_158([NPVs0[t][0] for t in range(0,sim)], [NPVs0[t][1] for t in range(0,sim)]).loc[:,""])

NPVs0 = []
for s in range(0,sim):
    temp = monte_carlo(n=def_n, mcr=def_mcr, e0=def_e0, e=def_e, p=def_p, q=def_q, r=def_r, r_mean=def_r_mean, r_sd=def_r_sd, gmmb=.9*def_gmmb)
    NPVs0.append(temp)
table_159_GMMB = list(table_158([NPVs0[t][0] for t in range(0,sim)], [NPVs0[t][1] for t in range(0,sim)]).loc[:,""])

table_159 = pd.DataFrame(data= {"Control": table_159_def, "Increase P": table_159_P, "Increase MC": table_159_MC, "Increase UAP": table_159_UAP, "Increase GMMB": table_159_GMMB}
                        ,index=["E[NPV]", "SD[NPV]", "95% CI for E[NPV]", "5th percentile"
                                , "Median of NPV", "95th percentile", "N-", "N*"])
print(table_159)
print(f"Completed in {round(time.time() - start, 2)} seconds.")