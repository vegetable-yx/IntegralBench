import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the Catalan constant
result = mp.catalan

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))