import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 6 to get the final result
result = pi_squared / 6

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))