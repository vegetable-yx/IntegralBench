import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Calculate ln(2) using mpmath's logarithm function
ln2 = mp.log(2)

# Compute π/2
pi_over_2 = pi_value / 2

# Multiply the components to get final result
result = pi_over_2 * ln2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))