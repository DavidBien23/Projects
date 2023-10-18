lam_null=.1
lam_alt=1
n=10
trials=10
num_R=100000
Rs=matrix(ncol=1,nrow=0)
for (i in 1:num_R){
  xi=rbinom(n,trials,lam_null)
  num=1/((exp(n*lam_alt))*prod(factorial(xi)))
  den=prod(choose(n,xi))*(lam_null^sum(xi))*((1-lam_null)^(n^2-sum(xi)))
  R=num/den
  Rs=rbind(R,Rs)
}
print(max(Rs))
hist(Rs)
(sum(Rs>2.56)/num_R)
yi=rbinom(10000,trials,lam_null)
hist(yi)
P_Value=matrix(ncol=1,nrow=0)
for (i in 1:num_R){
  l=sum(yi>Rs[i])/10000
  P_Value=rbind(P_Value,l)
}
hist(P_Value)
#Alternative Hypothesis
Ras=matrix(ncol=1,nrow=0)
for (i in 1:num_R){
  xai=rpois(n,lam_alt)
  num=1/((exp(n*lam_alt))*prod(factorial(xai)))
  den=prod(choose(n,xai))*(lam_null^sum(xai))*((1-lam_null)^(n^2-sum(xai)))
  R=num/den
  Ras=rbind(R,Ras)
}
print(max(Ras))
hist(Ras)
(sum(Ras>2.56)/num_R)
yai=rpois(10000,lam_alt)
hist(yai)
P_Value_a=matrix(ncol=1,nrow=0)
for (i in 1:num_R){
  l=sum(yai>Ras[i])/10000
  P_Value_a=rbind(P_Value_a,l)
}
hist(P_Value_a)