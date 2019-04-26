from __future__ import print_function

from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from ipywidgets import interact, interactive, fixed
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import adjusted_rand_score
from sklearn.cluster import KMeans
#matplotlib inline
import numpy as np
import pandas as pd
import numpy as np
import visualisation
import clustering
import plotly
import plotly.graph_objs as go
import ipywidgets as widgets

init_notebook_mode(connected=False)
# use seaborn plotting style defaults
doInteractive = True
def interactivePlots(fig, axes):
    # helper function to decide to use plotly interactive plots or not
    if(doInteractive):
        plotly.offline.iplot_mpl(fig, show_link=False, strip_style=True) # offline ipython notebook

#data
GuoDataAll = pd.read_csv('C://Documents//GuoData.csv', index_col=[0])
labelsAll = GuoDataAll.index # The labels give the cell-type for each cell

#Take the data subsdet containing only 64 cell stage labels
frames = [GuoDataAll.iloc[labelsAll=='64 TE',:],GuoDataAll.iloc[labelsAll=='64 EPI',:],
          GuoDataAll.iloc[labelsAll=='64 PE',:]]
GuoData = pd.concat(frames)
labels = GuoData.index
N, D = GuoData.shape
print('Cells: %s, Genes: %s'%(N, D))
GuoData.head()


kmeans = KMeans(n_clusters=3, random_state=0).fit(GuoData.values)
kmeanslabels = kmeans.labels_
print (kmeanslabels)
