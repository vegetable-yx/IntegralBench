import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to get the final result
result = pi_squared / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))