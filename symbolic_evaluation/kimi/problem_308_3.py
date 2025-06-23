import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π and ln(2) to get final result
result = pi_value * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))