import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 2 to get 2*sqrt(2)
two_sqrt2 = 2 * sqrt2

# Multiply by pi to get final result
result = two_sqrt2 * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))