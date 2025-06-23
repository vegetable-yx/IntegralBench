import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(2) and cos(2)
sin_2 = mp.sin(2)
cos_2 = mp.cos(2)

# Compute the terms inside the parentheses
term1 = sin_2 / 2
term2 = cos_2

# Combine terms and multiply by sqrt(2)/pi
combined_terms = term1 - term2
result = (mp.sqrt(2) / mp.pi) * combined_terms

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))