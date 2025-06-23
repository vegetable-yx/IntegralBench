import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate pi to the 5th power
pi_power_5 = mp.pi ** 5

# Divide by 810 to get the result
result = pi_power_5 / 810

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))