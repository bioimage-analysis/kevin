import matplotlib.pyplot as plt

def plot(image, blob, Title = ""):

    fig, axes = plt.subplots(1,1, figsize=(40, 30))
    fig.suptitle(Title,weight = "bold", fontsize=25, y = 0.88)
    axes.imshow(image, cmap='gray',interpolation='nearest')
    axes.scatter(blob[:,1], blob[:,0], marker='o', facecolors='none', edgecolors='r', label = "Counted Green Cells")
    axes.legend(loc=0, fontsize=25, shadow=True)
    axes.axis("off")
    axes.autoscale_view('tight')
    #fig.savefig('Counted_cell_Green.jpg')
