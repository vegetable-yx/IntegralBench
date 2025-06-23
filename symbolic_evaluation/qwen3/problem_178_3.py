import mpmath as mp
mp.dps = 15

# Calculate individual components
sqrt2 = mp.sqrt(2)
sin2 = mp.sin(2)
cos2 = mp.cos(2)

# Compute terms inside the parentheses
term1 = sin2 / 3
term2 = cos2 / 2
combined_terms = term1 - term2

# Multiply by sqrt(2)/pi
result = (sqrt2 / mp.pi) * combined_terms

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))