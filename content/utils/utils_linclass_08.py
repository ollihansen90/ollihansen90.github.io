import numpy as np
import matplotlib.pyplot as plt
from utils import Vektorfolge, Koordinatensystem, Gerade

def draw(w, data, label):
    size = 11
    config = {"size": size}
    koordinatensystem = Koordinatensystem(config)
    gewichtsvektor = w[:2]
    theta = w[-1]
    if w[1]==0:
        aufpunkt = np.array([(theta-gewichtsvektor[1])/gewichtsvektor[0],1])
    else:
        aufpunkt = np.array([1,(theta-gewichtsvektor[0])/gewichtsvektor[1]])
    gerade = Gerade(aufpunkt, gewichtsvektor[::-1]*np.array([1,-1]))
    vec = Vektorfolge([aufpunkt, gewichtsvektor], ["blue", "tab:green"], alphalist=[0,1])

    fig = plt.figure(figsize=[7,7])
    koordinatensystem.draw()
    gerade.draw(col="r")
    vec.draw()
    plt.scatter(data[label==1,0], data[label==1,1])
    plt.scatter(data[label==-1,0], data[label==-1,1])
    plt.axis("scaled");plt.xlim([-size,size]);plt.ylim([-size,size]);plt.axis("off")
    fig.canvas.draw()
    image_flat = np.frombuffer(fig.canvas.buffer_rgba(), dtype='uint8')
    image = image_flat.reshape(*reversed(fig.canvas.get_width_height()), 4)[...,:3]
    plt.close()
    return image