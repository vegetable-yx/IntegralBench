import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to get final result
result = pi_squared / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))