import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π and ln(2)
product = pi_value * ln2

# Divide the product by 8 to get final result
result = product / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))