#MonteCarlo
#to compare results: online calc:https://academo.org/demos/estimating-pi-monte-carlo/
import random as rd
import numpy as np
import matplotlib.pyplot as plt

n=10000000
pii=[]

zwischenergebnis= np.zeros(n)

def mc_pi(n): #calculates pi by creating n random points, returns pi
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


def mc_pi_stat(n,m): #appends m times of pi calculations, returns mean and std
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

def mc_pi_plt():
    a=100
    daten= np.zeros((5,3)) #creates 3D array column0: x-axis, column1: mean, column2: std
    for x in range(5):
        [mean,std]=mc_pi_stat(a,10)
        daten[x,0]=a
        daten[x,1]=mean
        daten[x,2]=std
        a = a * 10

    print(daten)
    plt.scatter(np.log10(daten[:,0]), daten[:, 1], color='red')
    plt.errorbar(np.log10(daten[:,0]), daten[:, 1], yerr=daten[:, 2])
    plt.title('Real values and errorbars')
    plt.show()

    plt.scatter(np.log10(daten[:,0]), np.log10(daten[:, 2]),color = 'yellow')
    #plt.show()
    xax=np.log10(daten[:,0])
    yax= np.log10(daten[:, 2])
    m,b = np.polyfit(xax,yax,1)
    plt.plot(xax,m*xax +b)
    plt.show()




#[mean, std] = mc_pi_stat(100, 10) #m-mal Berechnung ausführen
mc_pi_plt()

