import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Catalan's constant using mpmath's built-in constant
catalan_constant = mp.catalan

# Multiply by 2 to get the final result
result = 2 * catalan_constant

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))