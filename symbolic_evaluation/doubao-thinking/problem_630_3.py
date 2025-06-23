import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute π using mpmath's constant
pi_val = mp.pi

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Multiply π, sqrt(3), and ln(3) for the numerator
numerator = pi_val * sqrt3 * ln3

# Divide by 36 to get the final result
result = numerator / 36

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))