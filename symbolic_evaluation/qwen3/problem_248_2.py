import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate ln(2) using mpmath's logarithm function
ln2 = mp.log(2)

# Compute π/4
pi_over_4 = pi / 4

# Multiply components to get final result
result = pi_over_4 * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))