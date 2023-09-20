import pandas as pd
import numpy as np


print("How many classes (rows)? "); r = int(input())
print("How many observations (columns)? "); n = int(input())
data = np.array(input("Input Data seperated by spaces: ").split())

if data.size != r*n:
    print("The data does not match the row x column matrix. Please try again.")
else:
    data = data.reshape(r,n)
    df = pd.DataFrame(data, dtype="float64")
    
    # Calculate mu_hat.
    mu_i = []
    for i in range(0,r):
        mu_i.append(sum(df.loc[i])/n)
    mu_hat = sum(mu_i)/r
    print("\nmu_hat = ", mu_hat)

    # create a new dataframe for the variance of each observation.
    df2 = df
    for i in range(0,r):
        for j in range(0,n):
            df2.loc[i].at[j] = (df.loc[i].at[j] - mu_i[i])*(df.loc[i].at[j] - mu_i[i])
    
    # Then compute v_hat
    sam_v = []
    for i in range(0,r):
        sam_v.append(sum(df2.loc[i])/(n-1))
    v_hat = sum(sam_v)/r
    print("v_hat = ",v_hat)

    # Calculate a_bar then a_hat.
    a_i = []
    for i in range(0,r):
        a_i.append((mu_i[i] - mu_hat)*(mu_i[i] - mu_hat))
    a_hat = sum(a_i)/(r-1) - v_hat/n
    print("a_hat = ",a_hat)

    # Compute Z.
    Z = n/(n+v_hat/a_hat)
    print("Z = ",Z)

    # Compute Class predictions.
    for i in range(0,r):
        print("Class",i,": ",Z*mu_i[i] + (1-Z)*mu_hat)