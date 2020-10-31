# Stat503 - HW #1
# Written in Python 3.7.7
# Alexandru Ivan
# STID: 0027908411

# %%
# Import the pandas library
import pandas as pd

# Import graphing tool of your choice, there's like 10 good ones
import matplotlib.pyplot as plt

# %%
# Seeds Data Array (How many seeds germinated)
n_seeds_germinated = [11, 9, 20, 11, 23, 16, 16, 25, 24, 27, 27, 30]

# %%
# Temperature Data Array
soil_temp_celcius = [
    15.8,
    15.5,
    16.5,
    15.4,
    16.2,
    16.3,
    16.6,
    17.2,
    17.5,
    17.4,
    18.3,
    21.0,
]

# %%
# Make a dataframe of the two arrays above
dataframe = pd.DataFrame(
    list(zip(n_seeds_germinated, soil_temp_celcius)),
    columns=["Number_Germinated", "Soil_Temperature_Celcius"],
)
dataframe
dataframe.mean()

# %%
# A histogram of number of seeds germinated at various temperatures
plt.hist(n_seeds_germinated, bins=5)
plt.xlabel("Number of Seeds that Germinated")
plt.ylabel("Frequency")

# %%
# A histogram of how many samples were tested at various bins of temperatures
plt.hist(soil_temp_celcius, data=dataframe, bins=5)
plt.xlabel("Temperature In Celcius")
plt.ylabel("Number of Samples")

# %%
# Scatterplot of the different samples (number germinated in each sample)
#     plotted against the temperature
plt.scatter(x=dataframe.Soil_Temperature_Celcius, y=dataframe.Number_Germinated)
plt.xlabel("Temperature In Celcius")
plt.ylabel("Number of Seeds that Germinated")
