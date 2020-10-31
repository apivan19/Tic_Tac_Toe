# Stat503 - HW #4
# Written in Python 3.7
# Alexandru Ivan 
# STID: 0027908411

# import some packages for analyzing dataset
import numpy as np
import scipy.stats

# A function that finds that lower limit of the 95% CI, the point estimate, and the uppower limit of the 95% CI
def mean_confidence_interval(data, confidence=0.95):
    a = np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m-h, m, m+h

# Import the pandas library and seaborn for beautiful printing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load up the .csv file that we are using
data_frame = pd.read_csv("tibbetts_et_al_2019_wasp_ti.csv")
data_frame.head(23)

# Make the beautiful binomial plot... kinda. I actually made a histogram that has so many bins that it just looks like a binomial plot
# Hope this is ... acceptable
sns.distplot(data_frame["Correct"], hist=True, kde=False)
plt.show()

# Return and print the results of the function at the top functioning on the wasp correct dataset
lower, mid, upper = mean_confidence_interval(data = data_frame["Correct"])
print(lower, mid, upper)