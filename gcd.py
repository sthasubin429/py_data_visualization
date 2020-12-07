import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def calcGcd(a, b, numstep):

    if b == 0 or a ==0:
        return [a, numstep]
    else:
        return calcGcd(b, a % b, numstep + 1)

for i in range(1,10):
    numa = i
    for j in range(1,10):
        numb = j
        if numa > numb:
            a = numa
            b = numb
        else:
            a = numb
            b = numa
        ans = calcGcd(a,b,0)
        #print("GCD of {} and {} is {} takes {} steps".format(numa, numb, ans[0], ans[1]))




uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data, linewidth=0.5)
plt.show()
