import pandas as pd
import numpy as np


print("How many classes (rows)? "); r = int(input())
print("How many observations (columns)? "); n = int(input())
data = np.array(input("Input average claims seperated by spaces: ").split())
ms = np.array(input("Input exposure seperated by spaces: ").split())

if data.size & ms.size != r*n:
    print("The data does not match the row x column matrix. Please try again.")
else:
    data = data.reshape(r,n)
    ms = ms.reshape(r,n)
    df = pd.DataFrame(data, dtype="float64")
    df_ms = pd.DataFrame(ms, dtype="float64")
    
    # Calculate m_i & mu_i.
    m_i = []
    mu_i = []
    mx = []
    for i in range(0,r):
        m_temp = sum(df_ms.loc[i])
        xm = sum(df_ms.loc[i] * df.loc[i])

        m_i.append(m_temp)
        mu_i.append(xm/m_temp)
        mx.append(xm)
    m = sum(m_i)
    mu_hat = sum(mx)/m
    print("\nmu_hat = ", mu_hat)

    # create a new dataframe for the variance of each observation and compute v_hat.
    df2 = df
    for i in range(0,r):
        for j in range(0,n):
            df2.loc[i].at[j] = df_ms.loc[i].at[j]*( (df.loc[i].at[j] - mu_i[i])*(df.loc[i].at[j] - mu_i[i]) )
    
    v_hat = df.values.sum()/(r*(n-1))
    print("v_hat = ",v_hat)

    # Calculate a_bar then a_hat.
    if r == 1:
        x_bar = int(input("expected mean: "))
        a_hat = (mu_hat - x_bar)**2 - v_hat/m
    else:
        a_i = []
        for i in range(0,r):
            a_i.append(m_i[i]*(mu_i[i] - mu_hat)**2)
        a_i.append(-v_hat*(r-1))
        m_i2 = m - sum([i**2 for i in m_i])/m
        a_hat = sum(a_i)/m_i2
    print("a_hat = ",a_hat)

    # Compute Class predictions and credibility factors.
    k = v_hat/a_hat
    if r == 1:
        Z = m/(m+k)
        print(f"Class 1 prediction: ",Z*mu_hat + (1-Z)*x_bar, f"with credibility factor: {Z}.")
    else:
        for i in range(0,r):
            Zi = m_i[i]/(m_i[i]+k)
            print(f"Class {i+1} prediction: ",Zi*mu_i[i] + (1-Zi)*mu_hat, f"with credibility factor: {Zi}.")