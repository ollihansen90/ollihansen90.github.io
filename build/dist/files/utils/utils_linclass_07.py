import numpy as np
import matplotlib.pyplot as plt
from utils import Koordinatensystem, Gerade, Vektorfolge, generate_data

def draw1(gewichtsvektor=np.ones(2), theta=0, first=False):
    data = np.array([[3,6],[-2,7]])

    size = 11
    config = {"size": size}
    koordinatensystem = Koordinatensystem(config)
    #aufpunkt = # theta = normal@aufpunkt = n1a1+n2a2
    if gewichtsvektor[1]==0:
        aufpunkt = np.array([(theta-gewichtsvektor[1])/gewichtsvektor[0],1])
    else:
        aufpunkt = np.array([1,(theta-gewichtsvektor[0])/gewichtsvektor[1]])
    gerade = Gerade(aufpunkt, gewichtsvektor[::-1]*np.array([1,-1]))
    vec = Vektorfolge([aufpunkt, gewichtsvektor], ["blue", "tab:green"], alphalist=[0,1])

    plt.figure(figsize=[7,7])
    koordinatensystem.draw()
    if not first:
        gerade.draw()
        vec.draw()
    plt.plot(data[:,0], data[:,1], "ro", markersize=5)
    plt.axis("scaled");plt.xlim([-size,size]);plt.ylim([-size,size]);plt.axis("off")
    plt.show()
    #print(data)
    if not first:
        if gerade.on_gerade(data[0]) and gerade.on_gerade(data[1]):
            print(f"Sehr gut! Gewichtsvektor [{gewichtsvektor[0]},{gewichtsvektor[1]}] und  Schwellenwert {theta} sind korrekt!")
            return True
        else:
            print(f"Das stimmt leider noch nicht... Gewichtsvektor [{gewichtsvektor[0]},{gewichtsvektor[1]}] und Schwellenwert {theta} sind nicht richtig.")
            return False

def draw2(gewichtsvektor=np.ones(2), theta=0, first=False):
    data, label = generate_data()

    size = 11
    config = {"size": size}
    koordinatensystem = Koordinatensystem(config)
    #aufpunkt = # theta = normal@aufpunkt = n1a1+n2a2
    if gewichtsvektor[1]==0:
        aufpunkt = np.array([(theta-gewichtsvektor[1])/gewichtsvektor[0],1])
    else:
        aufpunkt = np.array([1,(theta-gewichtsvektor[0])/gewichtsvektor[1]])
    gerade = Gerade(aufpunkt, gewichtsvektor[::-1]*np.array([1,-1]))
    vec = Vektorfolge([aufpunkt, gewichtsvektor], ["blue", "tab:green"], alphalist=[0,1])

    plt.figure(figsize=[7,7])
    koordinatensystem.draw()
    if not first:
        gerade.draw(col="r")
        vec.draw()
    plt.scatter(data[label==1,0], data[label==1,1])
    plt.scatter(data[label==-1,0], data[label==-1,1])
    plt.axis("scaled");plt.xlim([-size,size]);plt.ylim([-size,size]);plt.axis("off")
    plt.show()
    if not first:
        out = np.sign(data[:,:2]@gewichtsvektor-theta)
        acc = np.mean(out==label)
        if acc==1:
            print(f"Sehr gut! Gewichtsvektor [{gewichtsvektor[0]},{gewichtsvektor[1]}] und  Schwellenwert {theta} sind korrekt!")
            return True
        else:
            print(f"Das stimmt leider noch nicht... Gewichtsvektor [{gewichtsvektor[0]},{gewichtsvektor[1]}] und Schwellenwert {theta} sind nicht richtig. \nDer Klassifikator hätte eine Genauigkeit von {acc*100}%, {int(len(label)*(1-acc))} Punkte werden also falsch klassifiziert.")
            return False