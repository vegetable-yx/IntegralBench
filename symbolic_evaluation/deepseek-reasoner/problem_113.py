import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))