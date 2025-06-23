import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the numerator (8 + pi squared)
numerator = 8 + pi_squared

# Divide by 12 to get the final result
result = numerator / 12

print(mp.nstr(result, n=10))