import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute π/6
pi_over_6 = pi_value / 6

# Multiply the components to get final result
result = pi_over_6 * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))