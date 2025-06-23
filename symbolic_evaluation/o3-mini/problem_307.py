import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve Catalan's constant from mpmath
catalan_constant = mp.catalan

# Multiply Catalan's constant by 2
result = 2 * catalan_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))