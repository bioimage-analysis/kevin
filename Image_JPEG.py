def save_img_jpeg(image, path, **kwargs):

    timeframes = kwargs.pop('timeframes', [])
    colors = kwargs.pop('colors', [])

    for j in colors:
        for i in timeframes:
            img = ((image[:,:,j, i]/image[:,:,j, i].max())*255).astype("uint8")
            if j == 0:
                io.imsave("{}/BF{}.jpg".format(path, i), img)
            elif j == 1:
                io.imsave("{}/Green{}.jpg".format(path, i), img)
            elif j == 2:
                io.imsave("{}/Red{}.jpg".format(path, i), img)
