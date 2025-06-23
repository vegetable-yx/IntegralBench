import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute fundamental components
sqrt2 = mp.sqrt(2)  # Calculate square root of 2
ln_term = mp.log(1 + sqrt2)  # Natural logarithm of (1 + sqrt(2))

# Break down the polynomial expression components
squared_log = ln_term**2  # Square of the logarithm term
linear_term = sqrt2 * ln_term  # sqrt(2) multiplied by logarithm term

# Calculate each part of the main expression
part1 = 3 * squared_log
part2 = 2 * linear_term
combined_expression = part1 - part2 + 1  # Combine all polynomial terms

# Final calculation with pi scaling
result = (mp.pi / 16) * combined_expression

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))