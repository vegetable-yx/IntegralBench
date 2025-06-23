import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute sinh(1) and multiply by 4
term1 = 4 * mp.sinh(1)

# Compute cosh(1) and multiply by 4
term2 = 4 * mp.cosh(1)

# Combine terms: 4*sinh(1) - 4*cosh(1) + 4
result = term1 - term2 + 4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))