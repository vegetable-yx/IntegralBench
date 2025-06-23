import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π and ln3
product = pi_value * ln3

# Divide the product by 8 to get final result
result = product / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))