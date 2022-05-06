import numpy as np
import matplotlib.pyplot as plt
import math
N= int(input("Enter no. of Seperate experiments:  "))
for k in range(N):
    n= int(input(" Enter no. of coins ="))
    deno = 2**n                                       # total microstate
    print("\nTotal no. of microstates for ",n," coins = ",deno)
    print("\nNo. of heads","       ","Probability of the macrostate")
    p = np.zeros(n+1)                                 # for size of array n+1
    prob = np.zeros(n+1)                              # for size of array n+1
    for i in range(n+1):
        p[i]=i
        num = math.factorial(n)/(math.factorial(p[i])*math.factorial(n-p[i]))    # microstates associated with a particular macrostate
        prob[i]=num/deno
        print(int(p[i]),"                   ",prob[i])
    plt.xlabel("No. of heads, n(h)", size=10)
    plt.ylabel("Probability, P(h)", size=10)
    plt.title("No. of coins = {}".format(n))
    plt.plot(p,prob)    
    plt.show()   

