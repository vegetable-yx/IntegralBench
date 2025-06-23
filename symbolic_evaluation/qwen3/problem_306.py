import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Catalan's constant is available in mpmath as mp.catalan
catalan_constant = mp.catalan

# Multiply Catalan's constant by 2
result = 2 * catalan_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))