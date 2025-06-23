import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate Catalan's constant using built-in function
catalan_constant = mp.catalan

# Multiply by 2 to get the final result
result = 2 * catalan_constant

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))