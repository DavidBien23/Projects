import numpy as np
data=input("Input data to be averaged seperated by spaces: ").split()
data=[int(x) for x in data]
step=float(input("Input desired accuracy: "))
result=[]
for i in np.arange(min(data)+step, max(data), step):
    temp=0
    for d in data:
        temp+=d-i
    result.append(abs(temp))

print(f"Dave's Average: {step*result.index(min(result))+min(data)+step}")
true=sum(data)/len(data)
print(f"True Average: {true}")
