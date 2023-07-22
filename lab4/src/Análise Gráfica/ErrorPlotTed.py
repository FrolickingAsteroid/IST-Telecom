#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotnine import *

Df = pd.read_csv("./DataDump/DataTed4.csv")
print(Df)

Df["N"]=Df["N"].values.astype(str)

plot = ggplot(Df) + \
    aes(x = "BW", y = "bit_errors", color = "N") + \
    geom_line(size = 2) + \
    geom_point(size = 3) + \
    theme_minimal()

print(plot)

