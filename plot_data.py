import matplotlib.pyplot as plt
import numpy as np

def plot(Green, Red, Title=""):

    Ratio = [x/y for x, y in zip(Green, Red)]
    y = np.array(Ratio)
    green = np.array(Green)
    red = np.array(Red)

    x = np.arange(0, 15*len(Ratio),15)

    z, res, _, _, _ = np.polyfit(x, y, 4, full=True)

    p = np.poly1d(z)

    crit = p.deriv().r
    r_crit = crit[crit.imag==0].real
    test = p.deriv(2)(r_crit)

    x_max = r_crit[test<0]
    y_max = p(x_max)

    fig, (axes) = plt.subplots(1, 2, figsize=(18, 9))
    fig.suptitle(Title,weight = "bold", fontsize=25, y = 0.96)
    xp = np.linspace(0, 1440, 100)
    for ax in axes:
        ax.set_xlabel("Time in min", fontsize=13)
        ax.set_ylabel("Ration Green/Red", fontsize=13)
    axes[0].plot(x, y, '.', label = "Ratio Green/Red")
    axes[0].plot(xp, p(xp), '-', label = "polynomial fit")
    #axes[0].plot( x_max, y_max, 'o', label = "Cycle = {} hrs".format(int(x_max/60)) )
    axes[0].legend(loc=0, shadow=True)
    axes[1].plot(x, green, label = "Number Green Cells")
    axes[1].plot(x, red, label = "Number Red Cells")
    axes[1].legend(loc=7, shadow=True)
    #fig.savefig('Result_First_Tile.jpg')
