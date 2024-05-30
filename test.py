import random
import matplotlib.pyplot as plt
import numpy as np




def Array_Generator():
    l=[]
    i=0
    while(i<50):
        l.append(random.randrange(1,100))
        i=i+1
    return l

def PlotingFunction(x,y):
    # plt.scatter(x, y)
    # plt.show()
    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 
    # poly1d_fn is now a function which takes in x and returns an estimate for y

    plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

    plt.xlim(1, 100)
    plt.ylim(1, 100)
    plt.show()
    

if __name__=="__main__":
    # print("Hello Main here")
    x=Array_Generator()
    y=Array_Generator()
    print(x)
    print(y)
    PlotingFunction(x,y)