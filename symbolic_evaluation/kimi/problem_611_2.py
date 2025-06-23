import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute 2 + sqrt(3)
term1_arg = 2 + sqrt3

# Natural logarithm of (2 + sqrt(3))
term1 = mp.log(term1_arg)

# Compute ln(3)
ln3 = mp.log(3)

# Compute (1/2) * ln(3) = 0.5 * ln(3)
term2 = 0.5 * ln3

# Final result: ln(2 + sqrt(3)) - (1/2)*ln(3)
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))