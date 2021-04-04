#MonteCarlo
#to compare results: online calc:https://academo.org/demos/estimating-pi-monte-carlo/
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import math
#n = input('Enter the size of random saples: ')
#print("Sample size is "+n)
#n = int(n)
n=10000000
#m=10
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
        #print("Zwischenergebnis ",zwischenergebnis[i])
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
        #print("pii array")
        #print(pii)
        x = x + 1
    mean=np.mean(pii)
    std=np.std(pii,ddof=1)
    print("Mittelwert:")
    print(mean)
    print("Abweichung:")
    print(std)
    return mean, std

#irgendwie springs aus der for schleife nach dem x=2. mal raus :(
#weil n zu klein war und der zero array somit nur 100 stellen hatte (x= 2 =100)
def mc_pi_plt():
    a=100
    daten= np.zeros((5,3))
    for x in range(5):
       # xachse = [0,0,0,0,0]
        #xachse[x]=a
        [mean,std]=mc_pi_stat(a,10)
        #daten[x,1]=mean
        #daten[x,2]=std
        daten[x,0]=a
        daten[x,1]=mean
        daten[x,2]=std
        a = a * 10

    print(daten)
    plt.scatter(np.log10(daten[:,0]), daten[:, 1], color='red')
    plt.errorbar(np.log10(daten[:,0]), daten[:, 1], yerr=daten[:, 2])
    plt.title('Real values and errorbars')
    plt.show()

    plt.scatter(np.log10(daten[:,0]), np.log10(daten[:, 2]))
    plt.show()





#[mean, std] = mc_pi_stat(10, 10) #m-mal Berechnung ausführen
#[mean, std] = mc_pi_stat(100, 10) #m-mal Berechnung ausführen
#[mean, std] = mc_pi_stat(1000, 10) #m-mal Berechnung ausführen
mc_pi_plt()

