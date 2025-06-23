import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate arcsin(1/4) using mpmath function
arcsin_term = mp.asin(mp.mpf(1)/4)

# Calculate square root of 15
sqrt_term = mp.sqrt(15)

# Combine terms according to the formula: arcsin(1/4) + sqrt(15) - 4
combined_terms = arcsin_term + sqrt_term - 4

# Multiply by π/2 to get final result
result = (mp.pi/2) * combined_terms

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))