import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate π/4 * ln(2)
term1 = (mp.pi / 4) * mp.log(2)

# Retrieve Catalan's constant (G)
term2 = mp.catalan

# Combine terms: result = π/4 * ln(2) - G
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))