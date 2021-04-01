#MonteCarlo
#to compare results: online calc:https://academo.org/demos/estimating-pi-monte-carlo/
import random as rd
import numpy as np

#n = input('Enter the size of random saples: ')
#print("Sample size is "+n)
#n = int(n)
n=5
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
        mc_pi_stat(zwischenergebnis)
        print("Zwischenergebnis ",zwischenergebnis[i])
    print("Final Estimation of Pi=", pi)


def mc_pi_stat(zwischenerg):
    global mittelwert
    mittelwert=np.mean(zwischenerg)
    print(mittelwert)




mc_pi(n)
print("Mittelwert ist:",mittelwert)
