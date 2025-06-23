import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π and ln(3)
product = pi_value * ln3

# Divide by 4 to get the final result
result = product / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))