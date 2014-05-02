import numpy as np
import matplotlib.pyplot as plt 

def plot_hist_and_show(array, bins=None):
  if not bins:
    bins = array.max()
  hist, bins = np.histogram(array, bins=bins)
  width = 0.7 * (bins[1] - bins[0]) 
  center = (bins[:-1] + bins[1:]) / 2 
  plt.bar(center, hist, align='center', width=width) 
  plt.show()

def plot2d_points_and_show(X):
  plt.scatter(X[:,0],X[:,1])
  plt.show()
