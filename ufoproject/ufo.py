#!/usr/bin/env python3

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

data = pd.read_csv('ufo_sighting_data.csv')

data_map = gpd.read_file('states/tl_2020_us_state.shp')

data_state = data['state/province'].value_counts().rename_axis('states').reset_index(name='counts')

data_state['states'] = data_state['states'].str.upper()

merged = data_map.set_index('STUSPS').join(data_state.set_index('states'))

var = 'counts'

fig, ax = plt.subplots(1, figsize=(10, 6))
plt.ylim(22, 51)
plt.xlim(-130, -65)
merged.plot(column=var, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')


plt.show()