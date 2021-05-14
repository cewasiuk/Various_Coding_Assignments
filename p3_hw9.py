#! /usr/bin/env python3 
#
#Gradschool Admissions
#
#1June2020
import numpy as np
#assuming a binomial distribution
print()
N = 787
Na = 146 
#Part (a)
#For such a distribution, can be approximated to be similar to Poisson
p = Na/N
mu = N*p
q = 1-p
sigma = np.sqrt(p*N*q)
print('The standard deviation of this population is', sigma)
print()

#Part (b)
#Uncertainty is jus sigma/applicants
unc = sigma/N
print('The uncertainty in the probability is', unc)
print()

#Part(c)
from scipy import stats 
newAdm = 48 
newGrp = 154
newmu = p*newGrp
newp = stats.binom.pmf(newAdm, N, p)#not entirely sure if I put in the right arguements
print('The probability that out of 154 participants, 48 more are admitted is', newp)
print()

#Part (d)
from scipy import special #errorfunction 
gaussian = 0.5*special.erfc(sigma / np.sqrt(2))
print('The resulting answer for the previous problem too small by a factor of', gaussian)
print()

#Part (e)
newnewp = 48 / 154 
newnewq = 1 - newnewp
newnewsigma = np.sqrt(N * newnewq * newnewp)
print("The best estimate for a group of 154 students is ", newnewp)
print('The standard deviation in the probability is ', newnewsigma)
print()

#Part (f)
n = 787 - 154
r = 146 - 48
pr = r / n
qr = 1 - pr
mur = pr * n 
sigmar = np.sqrt(n * pr * qr)
print('The admission probability for applicants in the remaining group is ', pr)
print('The standard deviation for the remaining group is ', sigmar)
print()

#Part (g)
import matplotlib.pyplot as plt
from scipy.stats import norm 
f1, ax1 = plt.subplots()
x = np.linspace(0, 787, 787)
y1 = norm.pdf(x, mu, sigma)
y2 = norm.pdf(x, newmu, newnewsigma)
y3 = norm.pdf(x, mur, sigmar)
plt.title('Probability of Gradschool Admissions for Specified Groupings')
ax1.set_xlim(0,180)
ax1.set_xlabel('Number of Admissions')
ax1.set_ylabel('Probability per Group')
ax1.plot(x, y1*787, color='red', label='Original Group Data')
ax1.plot(x, y2*154, color='blue', label='Smaller Group Data')
ax1.plot(x, y3*633, color='green', label='Remaing Group Data')
ax1.legend(loc = 'upper left')
f1.show()

input('\nPress <Enter> to exit...>\n')

