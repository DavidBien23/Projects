# Projects

<p>A collection of coding projects that I have created to make classwork easier, learn modules or 
functions, or practice the techniques I already know.</p>


### Bayes-Buhl_Straub_Estimation & Bayesian Empirical Estimation:

<p>During my college course dedicated to the Short Term Actuarial Mathematics (STAM), 
we learned about predicting the next claim from multiple given distribution of previous 
claims. We learned two methods for this as described by the file titles which included/excluded 
respectively the exposure of each claim. I create a file which would request user input 
on the number of claims in each category, amount per claim, and weight of exosure if necessary.</p>

### Dave's Life Contigent Actuarial Calculator (DLCAC):

<p>In contrast to the previous project where I worked on the short term, this project 
focused on the concepts of Long Term Actuarial Mathematics (LTAM). Ironically, the STAM 
project took only a week while the LTAM took about a month. The project is not finished and 
will not be as I have finished the class. The project taught me many things about python 
and I applied those techniques to other projects.</p>

### LC 15.4

<p>During my last semester of college and in the second section of LVC's ALTAM preparation
class, we were tasked to perform a Monte Carlo simulation of the NPV of an equity-linked
insurance policy with a Guaranteed Minimum Maturity Benefit (GMMB). I began by replicating 
previous tables that established the policy reserves and profit vector. From that, I could calculate 
the NPV and simulate 1000 alternative scenarios. I enjoyed refreshing my memory of python code and 
challegning myself to find a more efficient solution.</p>

### LC Exam Final

<p>This was my very last assigned group project for college and it was extensive. We look at a five-year
equity linked policy with $1,000,000 premium and survival based on a custom Makeham's Law. We find 
(a) The monthly risk premium with varying volitility, (b) the profit test of the policy, and the most 
difficult, (c) hedging amount and cash flows. For the project, we used Excel for organization but I 
independently reworked it as a python file to calculate the tedious NPV. I included our formal written document.</p>

### LC Review 3

<p>This is an update to the "LC 15.4" code that created a Monte Carlo simulation of an equity-linked
insurance policy. In my improvement, I made one instance of the simulation a function, called "monte_carlo(),
that relied on variables like renewal expenses, interest rates, premium amount, and a GMMB function. Using
the defined variabels, my function returns a NPV and GMMB (GMMB=0 if not applicable) as a tuple. Then, 
the update made it easy to complete the assignment a of analyzing the effects of changing specific variables. </p>

### Mean

<p>This is a small file that I worked on outside of school determined to find a unique way to 
average a list of numbers. My method chooses many values between the minimum and maximum of
the dataset then subtracts the data that are smaller than the chosen number and adds the data 
that are larger. After creating a list of sums, I find the smallest absolute value of difference
between the data and chosen point as the average. The user can input data and accuracy.</p>

### Teamwork 1

<p>This was a class teamwork assignment in preperation for the Statistical and Risk
Modelling (SRM) actuary exam where we analyze and choose the best variables for a linear 
model. The first half of the assignment was just manipulating parts of a linear model but 
second was to create our own linear model. We were given data from Boston crime statistics 
from the Intro to Stat Learning (ISLR2) library. We used forward selection and a transformation 
of the dependent variable to grow our model to just 4 of the 12 variables.</p>

### R-Assignment 5

<p>For my Statistical Inference class, we learned in depth statistical analysis including most 
likely estimators and Neaman-Pearson which this document analyzes. Along with the code is a formal
write-up of the assignment with explaniations and graphs included. The goal of this assignment was 
to find a significant test statistic and calculate the likelihood that the p value is significant. 
To properly test our test statistic, we need many iterations of samples which requires heavy computation.</p>
