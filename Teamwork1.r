#13a
set.seed(1)
x = rnorm(100)
#13b
eps = rnorm(100, sd = sqrt(0.25))
#13c
y = -1 + 0.5*x + eps
length(y)
#y is of length 100, beta_0 is -1 and beta_1 is 0.5
#13d
plot(x, y)
#there is a positive relationship between x and y. the estimates for both betas seem to be very close to the actual values
#13e
fit = lm(y~x)
summary(fit)
#the linear regression fits a model close to the true value of the coefficients as was constructed. the model has a large F-statistic with a near-zero p-value so the H0 can be rejected.
#13f
plot(x, y)
abline(fit, lwd=3, col="red")
abline(-1, 0.5, lwd=3, col="blue")
legend("topleft",c("Least Square", "Regression"), col=c("red","blue"), lty=c(1,1))
#13g
fit_sq = lm(y~x+I(x^2))
summary(fit_sq)
#there is evidence that model fit has increased over the training data given the slight increase in R^2 and RSE. but the p-value of the t-statistic suggests that there isn't a relationship between y and x^2.
#13h
set.seed(1)
eps1 = rnorm(100, 0, 0.05)
x1 = rnorm(100)
y1 = -1 + 0.5*x1 + eps1
plot(x1, y1)
lm.fit = lm(y1~x1)
summary(lm.fit)
abline(lm.fit, lwd=3, col="red")
abline(-1, 0.5, lwd=3, col="blue")
legend("topleft",c("Least Square", "Regression"), col=c("red","blue"), lty=c(1,1))
#the error seen in R^2 and the RSE both decrease significantly, which is expected
#13i
set.seed(1)
eps2 = rnorm(100, 0, 0.5)
x2 = rnorm(100)
y2 = -1 + 0.5*x2 + eps2
plot(x2, y2)
lm.fit2 = lm(y2~x2)
summary(lm.fit2)
abline(lm.fit2, lwd=3, col="red")
abline(-1, 0.5, lwd=3, col="blue")
legend("topleft",c("Least Square", "Regression"), col=c("red","blue"), lty=c(1,1))
#the error seen in R^2 and the RSE both increase significantly from part h, which is expected
#13j
confint(fit)
confint(lm.fit)
confint(lm.fit2)
#all intervals seem to be centered on about 0.5, with the second fit's interval being narrowest and the last fit's interval being widest
#Supplemental
library(ISLR2)
attach(Boston)
View(Boston)
pairs(Boston[,1:7])
lm.all=lm(crim~.,data=Boston)
summary(lm.all)
cor(Boston)
#Part a
lm.4=lm(crim~zn+dis+rad+medv,data=Boston)
summary(lm.4)
#Part b
lm.sqrt.dis=lm(crim~I(dis^0.5)+medv+rad+zn,data=Boston)
summary(lm.sqrt.dis)
lm.sqrt.zn=lm(crim~I(zn^0.5)+medv+rad+dis,data=Boston)
summary(lm.sqrt.zn)
#Part c
par(mar=c(1,1,1,1))
par(mfrow=c(2,2))
plot(lm.all)
#Part d
lm.sqrt.resp=lm(I(crim^0.5)~.,data=Boston)
summary(lm.sqrt.resp)
lm.ln.resp=lm(I(log(crim,base=exp(1)))~.,data=Boston)
lm.ln.resp.4=lm(I(log(crim,base=exp(1)))~zn+medv+dis+rad,data=Boston)
summary(lm.ln.resp)
Boston1=Boston[c(-381,-419,-406),]
lm.Boston1=lm(I(log(crim,base=exp(1)))~.,data=Boston1)
summary(lm.Boston1)
plot(lm.Boston1)