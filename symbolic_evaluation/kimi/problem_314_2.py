import mpmath as mp
mp.dps = 15

# Calculate the Catalan constant
G = mp.catalan

# Compute the negative of the Catalan constant
result = -G

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))