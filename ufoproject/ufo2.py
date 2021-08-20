#!/usr/bin/env python3
# -------------------------------------------------
# Created By  : Minh Ngu
# Created Date: 08/10/21
# Date Last Updated: 08/20/21
# version ='1.1'
# -------------------------------------------------
""" Choropleth Map of UAP sightings in the U.S.A """


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# imports UFO sightings data for the US
data = pd.read_csv('ufo_sighting_data.csv')

# imports shapefile of US states
data_map = gpd.read_file('states/tl_2020_us_state.shp')

# converts value_counts() output to dataframe
data_state = data['state/province'].value_counts().rename_axis('states').reset_index(name='counts')

# states codes in both dataframes are uppercase, so data_state needs to be set to uppercase
data_state['states'] = data_state['states'].str.upper()

# merges dataframe with shapefile
data_merged = data_map.set_index('STUSPS').join(data_state.set_index('states'))

# counts number of times each state appears
sightings = 'counts'


def main():
    fig, ax = plt.subplots(1, figsize=(16, 10))  # adjust display size of map
    plt.ylim(22, 51)  # limits scope of map
    plt.xlim(-130, -65)
    plt.axis("off")  # turns off axis display
    data_merged.plot(column=sightings,
                     legend=True,
                     marker='.',
                     markersize=20,
                     cmap='Purples',
                     linewidth=0.8,
                     ax=ax,
                     edgecolor='0.8')

    # labels each state with name
    data_merged.apply(lambda x: ax.annotate(text=x.NAME, xy=x.geometry.centroid.coords[0],
                                            ha='center', fontsize=5), axis=1)

    # creates and labels legend
    ax.legend(bbox_to_anchor=(1.28, 1.27), prop={'size': 8}, title="Number of Sightings")
    ax.set(title="UAP Sightings Heatmap")

    plt.show()


if __name__ == "__main__":
    main()
