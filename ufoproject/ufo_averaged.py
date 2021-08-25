#!/usr/bin/env python3
# -------------------------------------------------
# Created By  : Minh Ngu
# Created Date: 08/10/21
# Date Last Updated: 08/25/21
# version ='1.2'
# -------------------------------------------------
""" Choropleth Map of UAP sightings in the U.S.A """

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def data_import():
    # imports UFO sightings data for the US
    data_1 = pd.read_csv('ufo_sighting_data.csv')

    data_2 = pd.read_csv('state_pop.csv')

    # imports shapefile of US states
    data_map = gpd.read_file('states/tl_2020_us_state.shp')

    # converts value_counts() output to dataframe
    data_state = data_1['state/province'].value_counts().rename_axis('states').reset_index(name='counts')

    # states codes in both dataframes are uppercase, so data_state needs to be set to uppercase
    data_state['states'] = data_state['states'].str.upper()

    # merges dataframe with shapefile
    data_merged = data_map.set_index('STUSPS').join(data_state.set_index('states'))

    # counts number of times each state appears
    amount = 'counts'

    data_merged_pop = data_map.set_index('STUSPS').join(data_2.set_index('state_code'), rsuffix='POP')

    merged_1 = data_map.set_index('STUSPS').join(data_state.set_index('states'))
    merged_2 = merged_1.set_index('NAME').join(data_2.set_index('states'))

    merged_2['normalized_count'] = (merged_2['counts'] / merged_2['POP']) * 1000

    pop_size = 'POP'

    return data_merged, merged_1, amount, pop_size


def pop_import():

    data_1 = pd.read_csv('ufo_sighting_data.csv')

    data_2 = pd.read_csv('state_pop.csv')

    data_map = gpd.read_file('states/tl_2020_us_state.shp')

    #merged_pop = data_map.set_index('STUSPS').join(data.set_index('NAME'), rsuffix='POP')

    merged_1 = data_map.set_index('STUSPS').join(data_1.set_index('state/province'))
    merged_2 = merged_1.set_index('NAME').join(data_2.set_index('NAME'), rsuffix='POP')

    merged_2['normalized_count'] = (merged_2['count']/merged_2['POP']) * 1000

    pop_size = 'counts'

    return merged_2, pop_size


def sightings():
    data_merged, amount = data_import()
    fig, ax = plt.subplots(1, figsize=(16, 10))  # adjust display size of map
    plt.ylim(22, 51)  # limits scope of map
    plt.xlim(-130, -65)
    plt.axis("off")  # turns off axis display
    data_merged.plot(column=amount,
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
    ax.set(title="UAP Sightings Choropleth Map")

    plt.show()


def sightings_averaged():
    merged_2, pop_size = pop_import()
    fig, ax = plt.subplots(1, figsize=(16, 10))  # adjust display size of map
    plt.ylim(22, 51)  # limits scope of map
    plt.xlim(-130, -65)
    plt.axis("off")  # turns off axis display
    merged_2.plot(column=pop_size,
                              legend=True,
                              marker='.',
                              markersize=20,
                              cmap='Purples',
                              linewidth=0.8,
                              ax=ax,
                              edgecolor='0.8')

    # labels each state with name
    #merged_2.apply(lambda x: ax.annotate(text=x.NAME, xy=x.geometry.centroid.coords[0],
    #                                                 ha='center', fontsize=5), axis=1)

    # creates and labels legend
    ax.legend(bbox_to_anchor=(1.28, 1.27), prop={'size': 8}, title="Number of Sightings")
    ax.set(title="Normalized UAP Sightings Choropleth Map")

    plt.show()


if __name__ == "__main__":
    sightings()
    #sightings_averaged()
