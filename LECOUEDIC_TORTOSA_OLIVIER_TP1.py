#LECOUEDIC Thomas
#TORTOSA Hugo
#RAPHAEL OLIVIER
#TP1 DATA ANALYSIS

import matplotlib as plt
import statistics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from math import sqrt,pi,exp
from collections import Counter

#A
#1)
A = np.random.randint(0,10,1000)
#2)
plt.hist(A)
#3)
#mean
n = len(A)
S = sum(A)
mean = S / n
print(mean)
#median
A.sort()
if n % 2 == 0:
    m1 = A[n//2]
    m2 = n[n//2 - 1]
    median = (m1 + m2)/2
else:
    median = A[n//2]
print(median)
#mode
c = Counter(A) 
get_mode = dict(c) 
mode = [k for k, v in get_mode.items() if v == max(list(c.values()))] 
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is " + ', '.join(map(str, mode)) 
print(get_mode)
#4)
np.mean(A)
np.median(A)
#6)
#range
range1 = max(A)-min(A)
print(range1)
#variance
var=0
c=0
for k in range(0,n):
    c+=(A[k]-mean)**2
var = c/n
print(var)
#standard_deviation
std = math.sqrt(c/n)

np.ptp(A)
np.var(A)
np.std(A)

#B
#1
dataset = [10,5,12,8,48,9,23,10,24,11,48,12,9,13,7,14,13,16]
ser = pd.Series(dataset[1::2],index=dataset[::2])
ser.plot.bar()
#2
#position
np.mean(ser.index)
max(ser.index)
np.median(ser.index)
min(ser.index)
#dispersion
np.std(ser.index)
np.ptp(ser.index)
np.var(ser.index)
statistics.mode(ser.index)

#C
#1
#2
sampleQI = np.random.normal(100,15,100000)
plt.hist(sampleQI)
#3
np.mean(sampleQI)
np.std(sampleQI)
#4
cnt1 = 0
for i in sampleQI:
    if i<60:
        cnt1+=1
cnt1/len(sampleQI)*100
#5
cnt2 = 0
for i in sampleQI:
    if i>130:
        cnt2+=1
cnt2/len(sampleQI)*100
#6
def IC(mean, std):
    print('The percentage between', mean -1.96*std,"and",mean +1.96*std)
IC(np.mean(sampleQI),np.std(sampleQI))
#D
#1
sample1 = np.random.normal(100,15,10)
sample2 = np.random.normal(100,15,1000)
sample3 = np.random.normal(100,15,100000)
np.mean(sample1)
np.std(sample1)
np.mean(sample2)
np.std(sample2)
np.mean(sample3)
np.std(sample3)
IC(np.mean(sample1),np.std(sample1))
IC(np.mean(sample2),np.std(sample2))
IC(np.mean(sample3),np.std(sample3))
#2
dataset_malnutrition = read_csv(malnutrition.csv)
#3
np.mean(dataset_malnutrition)
np.std(datset_malnutrition)
IC(np.mean(dataset_malnutrition),np.std(dataset_malnutrition))









