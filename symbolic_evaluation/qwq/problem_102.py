import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 24 to obtain the final result
result = pi_squared / 24

# Print result with 10 decimal places
print(mp.nstr(result, n=10))