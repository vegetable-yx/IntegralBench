import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root term
sqrt_term = mp.sqrt(15) / 2

# Calculate the arcsin component
arcsin_value = mp.asin(1/4)
arcsin_component = 7 * arcsin_value

# Combine components for final result
result = sqrt_term - arcsin_component

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))