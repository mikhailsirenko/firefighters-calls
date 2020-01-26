from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.offsetbox import (OffsetImage,AnchoredOffsetbox)
# import os

def watermark(fig, ax, loc=2, downscale=8):
    # print(os.getcwd())
    img = Image.open('../references/tu_delft_logo.png')
    width, height = ax.figure.get_size_inches()*fig.dpi
    wm_width = int(width/downscale) # make the watermark 1/4 of the figure size
    scaling = (wm_width / float(img.size[0]))
    wm_height = int(float(img.size[1])*float(scaling))
    img = img.resize((wm_width, wm_height), Image.ANTIALIAS)

    imagebox = OffsetImage(img, zoom=1, alpha=0.5)
    imagebox.image.axes = ax

    ao = AnchoredOffsetbox(loc=loc, pad=0.01, borderpad=0, child=imagebox)
    ao.patch.set_alpha(0)
    ax.add_artist(ao)