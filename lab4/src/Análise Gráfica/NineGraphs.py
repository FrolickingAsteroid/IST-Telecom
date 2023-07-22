#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotnine import *

df = pd.read_csv("./DataDump/Desktop/cutie_data/QPSK small/data143_QPSK_TEDKp43415.csv")

df["BW"]=df["BW"].values.astype(str)

Genial = df.pivot_table('bit_errors','BW', 'N')

Genial.reset_index( drop=False, inplace=True )
Genial.reindex(['BW'], axis=1)
print(Genial)

# ---- from gallery ----

# Initialize the figure style
plt.style.use('seaborn-v0_8-dark-palette')
 
# create a color palette
palette = plt.get_cmap('coolwarm')
 
# multiple line plot
num=0
for column in Genial.drop('BW', axis=1):
    num+=1
 
    # Find the right spot on the plot
    plt.subplot(3,3, num)

    for v in Genial.drop('BW', axis=1):
        plt.plot(Genial['BW'], Genial[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
 
    # Plot the lineplot
    plt.plot(Genial['BW'], Genial[column], marker='', color=palette(num), linewidth=0.9, alpha=0.9, label=column)
 
    # Same limits for every chart
    plt.xlim(0,43)
    plt.ylim(0,140)

    #plt.xlabel('Loop Bandwidth', labelpad=-10)
    plt.ylabel('Number of Bit Errors')
    plt.xticks(ticks = [0.006,0.138,0.21,0.252], fontsize = 6, rotation=45)
 
    
     
 
    # Add title
    plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )
 
# Show the graph
plt.show()
