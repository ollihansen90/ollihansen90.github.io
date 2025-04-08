import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from IPython.display import display
from PIL import Image
from IPython.display import Image as Image_

class Koordinatensystem():
    def __init__(self, config={}):
        self.config = {
            "size": 11,
            "grid_alpha": 0.1,
            }
        self.config.update(config)

    def draw(self):
        size = self.config["size"]
        grid_alpha = self.config["grid_alpha"]
        plt.plot([0,0], [-size,size], "k")
        plt.plot([-size,size], [0,0], "k")
        for t in range(1,size):
            plt.plot([t,t], [-size,size], "k", alpha=grid_alpha)
            plt.plot([-t,-t], [-size,size], "k", alpha=grid_alpha)
            plt.plot([-size,size], [t,t], "k", alpha=grid_alpha)
            plt.plot([-size,size], [-t,-t], "k", alpha=grid_alpha)
            if t%2==0:
                plt.plot([t,t], [-0.1,0.1], "k")
                plt.text(t,-0.5, str(t), {"horizontalalignment":"center", "verticalalignment":"center"})
                plt.plot([-t,-t], [-0.1,0.1], "k")
                plt.text(-t,-0.5, str(-t), {"horizontalalignment":"center", "verticalalignment":"center"})
                plt.plot([-0.1,0.1], [t,t], "k")
                plt.text(-0.4, -t, str(-t), {"horizontalalignment":"right", "verticalalignment":"center"})
                plt.plot([-0.1,0.1], [-t,-t], "k")
                plt.text(-0.4, t, str(t), {"horizontalalignment":"right", "verticalalignment":"center"})
        plt.plot([-0.1,0,0.1], [size-0.2,size,(size-0.2)], "k")
        plt.plot([(size-0.2),size,(size-0.2)], [-0.1,0,0.1], "k")
        plt.plot([-0.1,0,0.1], [-(size-0.2),-size,-(size-0.2)], "k")
        plt.plot([-(size-0.2),-size,-(size-0.2)], [-0.1,0,0.1], "k")
        plt.text(-0.4, (size-0.2), "y", {"horizontalalignment":"center", "verticalalignment":"center"})
        plt.text(size, -0.4, "x", {"horizontalalignment":"center", "verticalalignment":"center"})

class Vektorfolge():
    def __init__(self, veclist, colorlist=list(mcolors.TABLEAU_COLORS.keys()), alphalist=None):
        self.veclist = veclist
        self.colorlist = colorlist
        self.alphalist = [1]*len(veclist) if alphalist==None else alphalist
        self.config = {"angles":'xy', "scale_units":'xy', "scale":1, "width":0.005, "zorder":2}

    def draw(self):
        plt.quiver(0,0,*self.veclist[0],**self.config, color=self.colorlist[0], alpha=self.alphalist[0])
        v = self.veclist[0].copy()
        for i in range(1, len(self.veclist)):
            plt.quiver(
                *v,
                *self.veclist[(i)],
                **self.config,
                color=self.colorlist[(i)%len(self.colorlist)],
                alpha=self.alphalist[i]
                )
            v += self.veclist[i].copy()

class Gerade():
    def __init__(self, aufpunkt, richtung):
        assert aufpunkt.shape==np.zeros(2).shape, "Der Vektor für den Aufpunkt hat nicht die richtige Form."
        assert richtung.shape==np.zeros(2).shape, "Der Vektor für die Richtung hat nicht die richtige Form."
        assert np.sum(np.abs(richtung))>0, "Der Vektor darf nicht [0,0] sein."
        self.aufpunkt = aufpunkt
        self.richtung = richtung

    def draw(self, col="tab:blue"):
        size = 11
        ecke1 = self.aufpunkt.copy()
        while np.max(np.abs(ecke1))<=size:
            ecke1 += self.richtung
        ecke2 = self.aufpunkt.copy()
        while np.max(np.abs(ecke2))<=size:
            ecke2 -= self.richtung
        ecken = np.stack([ecke1, ecke2])
        plt.plot(ecken[:,0], ecken[:,1], col)

    def on_gerade(self, pt):
        p = pt.copy().astype(float)
        p -= self.aufpunkt
        if np.sum(p**2)==0:
            return True
        p /= np.linalg.norm(p)
        return np.abs((self.richtung/np.linalg.norm(self.richtung))@p)>1-1e-6

def generate_data():
    np.random.seed(1)

    N = 100
    data = 3*np.random.randn(N,2)
    data[:N//2] += np.array([-4,6])
    data[N//2:] += np.array([2,-8])
    data = np.column_stack([data, -np.ones(N)])
    label = np.array(N//2*[1]+N//2*[-1])

    # Permutiere Daten
    perm = np.random.permutation(len(label))
    data = data[perm]
    label = label[perm]

    return data, label

def show_vid(vid):
    every = max((len(vid)//50, 1))
    vid = np.stack(vid[::every])
    vid = [Image.fromarray(img) for img in vid]
    vid[0].save("array.gif", save_all=True, append_images=vid[1:], duration=50, loop=0)

    with open('/content/array.gif','rb') as f:
        display(Image_(data=f.read(), format='gif'))