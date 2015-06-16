import numpy as np
import matplotlib.pyplot as plt 

def plot_image_hist_and_show(img, img2=None):
  if len(img.shape) != 2 or (img2 != None and len(img2.shape) != 2):
    raise ValueError("img must have 2 dimensions.")
  tup = np.histogram(img.ravel(), 256, (0,256))
  center = tup[1][:-1]
  hist = tup[0]
  hist[hist == 0] = 1
  hist = hist/float(hist.max())
  ax = plt.subplot(2,1,1)
  ax.bar(center, hist, align='center')
  ax.autoscale(tight=True)
  if img2 != None:
    ax2 = plt.subplot(2,1,2)
    tup = np.histogram(img2.ravel(), 256, (0,256))
    center = tup[1][:-1]
    hist = tup[0]
    hist[hist == 0] = 1
    hist = hist/float(hist.max())
    ax2.bar(center, hist, align='center')
    ax2.autoscale(tight=True)
  plt.show()

def plot_hist_and_show(array, bins=None, range_=None):
  if not bins:
    bins = array.max()-array.min()+1
  hist, bins = np.histogram(array, bins=bins, range=range_)
  width = 0.7 * (bins[1] - bins[0]) 
  center = (bins[:-1] + bins[1:]) / 2 
  plt.bar(center, hist, align='center', width=width) 
  plt.show()

def plot2d_points_and_show(X):
  plt.scatter(X[:,0],X[:,1])
  plt.show()

def plot_line(p1, p2, lw=2):
  plt.plot([p1[0],p2[0]], [p1[1],p2[1]], 'k-', lw=lw)

def plot_curve(x,y):
  plt.plot(x,y)
  plt.show()
