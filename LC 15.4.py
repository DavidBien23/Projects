import numpy as np
import pandas as pd
import statistics as st
import math as mt



n=10
i=.09
mcr=.0075
p = 5000
q = .005
r = .15
r_mean = .074928
r_sd = .15


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
start = {"t": [1], "APt": [.95*p], "F(t-1)": [0], "Ft-": [.95*p*inc0], "MCt": [mcr*(0+.95*p)*inc0], "Ft": [(1-mcr)*(.95*p)*inc0]}
table_151 = pd.DataFrame(data=start)
for s in range(1,n):
    next = {"t": [1+s], "APt": [.99*p], "F(t-1)": [table_151.at[s-1, "Ft"]], "Ft-": [(.99*p+table_151.at[s-1, "Ft"])*sim_r[s]]
            , "MCt": [mcr*(table_151.at[s-1, "Ft"]+.99*p)*sim_r[s]], "Ft": [(1-mcr)*(table_151.at[s-1, "Ft"]+.99*p)*sim_r[s]]}
    table_151 = pd.concat([table_151, pd.DataFrame(next)], ignore_index=True)
# Add a t=0 row
table_151 = pd.concat([pd.DataFrame({"t": [0], "APt": [0], "F(t-1)": [0], "Ft-": [0], "MCt": [0], "Ft": [0]}), table_151], ignore_index=True)

# Include  variables from table 15.2
extra = pd.DataFrame({"UAPt": [0]+list(5000-table_151.loc[1:10,"APt"]), "Et": list((.1*p+150, 0))+[.005*p for s in range(1,10)]
                      , "EDBt": list(.005*.1*table_151.loc[:,"Ft"])})
extra2 = pd.DataFrame(data={"It": [0]+list(.06*(extra.loc[1:10,"UAPt"]-extra.loc[1:10,"Et"]))})
extra3 = pd.DataFrame(data={"Prt": list(extra.loc[:,"UAPt"]-extra.loc[:,"Et"]+extra2.loc[:,"It"]+table_151.loc[:,"MCt"]-extra.loc[:,"EDBt"])})
extra3.at[10,"Prt"] = (extra3.at[10,"Prt"] - (1-q)*max(50000-table_151.at[10,"Ft"],0))

# Include variables from table 15.3
pif=pd.DataFrame(data={"PIF": [1]+[1]+[pow(1-q,1)*.9]+[pow(1-q,2)*.9*.95]
                          +[pow(1-q,t)*.9*.95 for t in range(3,10)]})
extra4=pd.DataFrame(data={"Πt": list(extra3.loc[:,"Prt"]*pif.loc[:,"PIF"])})

# Combination of table 15.1, 15.2, and 15.3
table_agg = table_151.join(extra).join(extra2).join(extra3).join(extra4).join(sim_rt)
print(table_agg)
print(table_agg[["sim_rt", "MCt", "Ft", "Prt", "Πt"]])

# Calculate the GMMB if it is < $50,000
GMMB = (1-q)*max(50000-table_agg.at[10,"Ft"],0); print(f"GMMB: {GMMB}.")

# Calculate the NPV
NPV = print(f"NPV: {sum([table_agg.at[t, 'Πt']*pow(1+r,-t) for t in range(0,11)])}.")


# Simulate many policies
sim = 1000
NPVs = []
Fts = []
for s in range(0,sim):
    sim_rs=[]
    for s in range(0,n+1) :
        sim_rs.append(np.random.lognormal(r_mean, r_sd))
    sim_rts = pd.DataFrame(data={"sim_rt": sim_rs})
    # Variable interest
    inc0s = sim_rs[0]

    # Table 15.1 using constant or random interest rates
    starts = {"t": [1], "APt": [.95*p], "F(t-1)": [0], "Ft-": [.95*p*inc0s], "MCt": [mcr*(0+.95*p)*inc0s], "Ft": [(1-mcr)*(.95*p)*inc0s]}
    table_151s = pd.DataFrame(data=starts)
    for s in range(1,n):
        nexts = {"t": [1+s], "APt": [.99*p], "F(t-1)": [table_151s.at[s-1, "Ft"]], "Ft-": [(.99*p+table_151s.at[s-1, "Ft"])*sim_rs[s]]
                , "MCt": [mcr*(table_151s.at[s-1, "Ft"]+.99*p)*sim_rs[s]], "Ft": [(1-mcr)*(table_151s.at[s-1, "Ft"]+.99*p)*sim_rs[s]]}
        table_151s = pd.concat([table_151s, pd.DataFrame(nexts)], ignore_index=True)

    # Add a t=0 row
    table_151s = pd.concat([pd.DataFrame({"t": [0], "APt": [0], "F(t-1)": [0], "Ft-": [0], "MCt": [0], "Ft": [0]}), table_151s], ignore_index=True)
    Fts.append(table_151s.at[10,"Ft"])

    # Include  variables from table 15.2
    extras = pd.DataFrame({"UAPt": [0]+list(5000-table_151s.loc[1:10,"APt"]), "Et": list((.1*p+150, 0))+[.005*p for s in range(1,10)]
                          , "EDBt": list(.005*.1*table_151s.loc[:,"Ft"])})
    extra2s = pd.DataFrame(data={"It": [0]+list(.06*(extras.loc[1:10,"UAPt"]-extras.loc[1:10,"Et"]))})
    extra3s = pd.DataFrame(data={"Prt": list(extras.loc[:,"UAPt"]-extras.loc[:,"Et"]+extra2s.loc[:,"It"]+table_151s.loc[:,"MCt"]-extras.loc[:,"EDBt"])})
    extra3s.at[10,"Prt"] = (extra3s.at[10,"Prt"] - (1-q)*max(50000-table_151s.at[10,"Ft"],0))

    # Include variables from table 15.3
    pifs=pd.DataFrame(data={"PIF": [1]+[1]+[pow(1-q,1)*.9]+[pow(1-q,2)*.9*.95]
                              +[pow(1-q,t)*.9*.95 for t in range(3,10)]})
    extra4s=pd.DataFrame(data={"Πt": list(extra3s.loc[:,"Prt"]*pifs.loc[:,"PIF"])})

    # Calculate the NPV
    NPVs.append(sum([extra4s.at[t, 'Πt']*pow(1+r,-t) for t in range(0,11)]))
table_158 = pd.DataFrame(data=[st.mean(NPVs), np.std(NPVs)
                               , (st.mean(NPVs)-1.96*st.stdev(NPVs)/mt.sqrt(sim), st.mean(NPVs)+1.96*st.stdev(NPVs)/mt.sqrt(sim))
                               , np.percentile(NPVs, 5), st.median(NPVs), np.percentile(NPVs, 95), sum([NPVs[t]<0 for t in range(0,sim)])
                               , sum([Fts[t]>50000 for t in range(0,sim)])]
                         , index=["E[NPV]", "SD[NPV]", "95% CI for E[NPV]", "5th percentile"
                                  , "Median of NPV", "95th percentile", "N-", "N*"]
                         , columns= [""])
print(table_158)