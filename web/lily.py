import pickle
import numpy as np
import gmplot # you need to install this from the above link
gmap=gmplot.GoogleMapPlotter(47.6097,-122.3331,13) # this centers the map in seattle

locs=pickle.load(open('./blockfacelocs.p','rb')) # load location data
clusterlocs=np.asarray(locs.values())
for b in range(np.size(clusterlocs,0)):
   gmap.polygon([clusterlocs[b,1],clusterlocs[b,3]],[clusterlocs[b,0],
                   clusterlocs[b,2]],color='r',edge_width=3)

st="index.html"
gmap.draw(st)
