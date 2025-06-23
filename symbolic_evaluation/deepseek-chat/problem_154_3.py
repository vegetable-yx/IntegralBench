import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Retrieve the Catalan constant from mpmath
G = mp.catalan

# Calculate half of the Catalan constant
result = G / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))