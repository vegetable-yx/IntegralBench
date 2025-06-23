import mpmath as mp
# Set precision to 15 decimal places
mp.dps = 15

# Calculate Catalan's constant
catalan = mp.catalan

# Multiply by 2 to get the result
result = 2 * catalan

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))