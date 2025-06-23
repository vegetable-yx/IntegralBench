import mpmath as mp

# Set decimal precision for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate ln(2) using mpmath's logarithm function
ln2 = mp.log(2)

# Compute π/4
pi_over_4 = pi / 4

# Multiply π/4 by ln(2) to get the final result
result = pi_over_4 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))