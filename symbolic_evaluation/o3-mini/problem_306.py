import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute 2 times the Catalan constant
result = 2 * mp.catalan

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))