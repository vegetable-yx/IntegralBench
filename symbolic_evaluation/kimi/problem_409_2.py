import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute π/4 using mpmath's constant
pi_over_4 = mp.pi / 4

# Compute natural logarithm of 2 using mpmath
ln2 = mp.log(2)

# Calculate (1/2) * ln(2)
half_ln2 = 0.5 * ln2

# Combine results for final calculation
result = pi_over_4 - half_ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))