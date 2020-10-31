import pandas as pd
# Note: Change = afterDrink - beforeDrink
data_frame = pd.read_csv("lefevre_2010_moqsuitos_and_beer.csv")
data_frame = data_frame.drop(columns = ["id"])
data_frame

# Data frame for just the beer drinkers
beer_df = data_frame[data_frame.drink=="beer"]
beer_df
# Data Frame for just the water drinkers
h2o_df = data_frame[data_frame.drink=="water"]
h2o_df

from dataprep.eda import plot
# Make a box plot of the data and a line plot of the data - These are the best way to get a good picture of the data
box_plot_line_plot = plot(data_frame, x="drink", y="change")

# make figures of each separately
plot(h2o_df, "change")

# TIME FOR A T-TEST!
import numpy as np
from scipy import stats

# Numpy Array of the CHANGES of the two groups
beer_change_array=beer_df.iloc[:18,4].values
beer_change_array
len(beer_change_array)
h2o_change_array=h2o_df.iloc[:,4].values
h2o_change_array
len(h2o_change_array)

# Calculate the variance to get the standard deviation
var_h2o = h2o_change_array.var(ddof=1)
var_beer = beer_change_array.var(ddof=1)

# Standard Deviation
std_dev = np.sqrt((var_h2o + var_beer)/2)

## Calculate the t-statistics
t = (h2o_change_array.mean() - beer_change_array.mean())/(std_dev*np.sqrt(2/25))
t

#Degrees of freedom / not the be confused with df for data_frame
df = 2*18 - 2

#p-value after comparison with the t 
p = stats.t.cdf(t,df=df)
p

