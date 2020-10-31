from scipy.stats import norm

estimate = norm.cdf(98.8, 98.6, 0.6)
prob_of_temp_above_998 = 1 - estimate

sample_temperature_above_998 = 11 / 500

# Basically the same, so we shouldn't be
