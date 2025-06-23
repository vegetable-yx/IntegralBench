import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the first term: 2 * pi * Catalan's constant (G)
term1 = 2 * mp.pi * mp.catalan

# Calculate the second term: (7/2) * zeta(3)
term2 = (7 / 2) * mp.zeta(3)

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))