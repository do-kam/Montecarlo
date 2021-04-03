#MonteCarlo
#to compare results: online calc:https://academo.org/demos/estimating-pi-monte-carlo/
import random as rd
import numpy as np

#n = input('Enter the size of random saples: ')
#print("Sample size is "+n)
#n = int(n)
n=100
m=10
pii=[]

zwischenergebnis= np.zeros(n)

def mc_pi(n):
    circlepoints = 0
    squarepoints = 0
    for i in range (0,n):
        randx = rd.uniform(0, 1)
        randy = rd.uniform(0, 1)
        distance= randx**2 + randy**2
        if (distance<1):
            circlepoints +=1

        squarepoints +=1

        pi = 4* circlepoints/ squarepoints
        #global zwischenergebnis
        zwischenergebnis[i]=pi
       # mc_pi(zwischenergebnis)
        print("Zwischenergebnis ",zwischenergebnis[i])
    print("Final Estimation of Pi=", pi)
    return[pi]


#def mc_pi_stat(zwischenerg):
    #global mittelwert
    #mittelwert=np.mean(zwischenerg)
    #print(mittelwert)


#def mc_pi_stat(n,m):
#    mc_pi(n)
#    x=0
#    while x<m:
#        pii.append(mc_pi(n))
#        x=x+1
#        mean =np.mean(pii)
#        std = np.std(pii,ddof=1)
#        return mean,std


def mc_pi_stat(n,m):
    x=0
    while x<m:
        pii.append(mc_pi(n))
        print("pii array")
        print(pii)
        x = x + 1
    mean=np.mean(pii)
    std=np.std(pii,ddof=1)
    print("Mittelwert:")
    print(mean)
    print("Abweichung:")
    print(std)
    return mean, std





#mc_pi(n)
#mc_pi_stat(n,m)
[mean, std] = mc_pi_stat(100, 10) #m-mal Berechnung ausführen
#print("Mittelwert ist:",mittelwert)
