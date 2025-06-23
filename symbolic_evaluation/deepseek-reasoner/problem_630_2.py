import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Get the constant pi
pi_val = mp.pi

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Calculate numerator: sqrt(3) * pi * ln(3)
numerator = sqrt3 * pi_val * ln3

# Divide by 36 to get the final result
result = numerator / 36

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))