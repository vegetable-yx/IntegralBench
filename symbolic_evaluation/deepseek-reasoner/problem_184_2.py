import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Compute the final result (π * ln3)/8
result = (pi_value * ln3) / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))