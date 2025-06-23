import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the fourth power
pi_power_4 = mp.pi ** 4

# Divide by 120 to get the final result
result = pi_power_4 / 120

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))