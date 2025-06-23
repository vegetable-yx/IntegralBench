import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply π² by √2
numerator = pi_sq * sqrt_2

# Divide by 2 to get final result
result = numerator / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))