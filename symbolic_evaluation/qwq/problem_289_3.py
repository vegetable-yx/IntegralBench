import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate ln(2) using mpmath's logarithm function
ln2 = mp.log(2)

# Compute π/4 * ln(2) using exact fractions
pi_over_4 = mp.fdiv(pi, 4)
result = mp.fmul(pi_over_4, ln2)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))