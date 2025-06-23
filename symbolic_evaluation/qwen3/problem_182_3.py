import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute natural logarithm term: ln(2 + sqrt(5))
log_term = mp.log(2 + sqrt5)

# Calculate the fractional component: (1 - sqrt(5))/2
fraction = (1 - sqrt5) / 2

# Combine components and multiply by pi
result = mp.pi * (log_term + fraction)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))