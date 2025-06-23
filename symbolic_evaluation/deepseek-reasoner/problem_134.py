import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get pi constant
pi_val = mp.pi

# Multiply components to get final result
result = sqrt2 * pi_val

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))