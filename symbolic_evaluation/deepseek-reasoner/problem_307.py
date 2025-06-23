import mpmath as mp
mp.dps = 15

# Calculate Catalan's constant using built-in constant
catalan = mp.catalan

# Multiply by 2 to get the final result
result = 2 * catalan

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))