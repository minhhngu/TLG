#!/usr/bin/env python3

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


data = pd.read_csv('ufo_sighting_data.csv')

data_map = gpd.read_file('states/tl_2020_us_state.shp')

data_state = data['state/province'].value_counts().rename_axis('states').reset_index(name='counts')

data_state['states'] = data_state['states'].str.upper()

data_merged = data_map.set_index('STUSPS').join(data_state.set_index('states'))

var = 'counts'

fig, ax = plt.subplots(1, figsize=(10, 6))
plt.ylim(22, 51)
plt.xlim(-130, -65)
data_merged.plot(column=var,
                 legend=True,
                 marker='.',
                 markersize=20,
                 cmap='Purples',
                 linewidth=0.8,
                 ax=ax,
                 edgecolor='0.8')

ax.legend(bbox_to_anchor=(1.4, 1.25), prop={'size': 12}, title="Number of Sightings")
ax.set(title="UFO Sightings Heatmap")

plt.show()