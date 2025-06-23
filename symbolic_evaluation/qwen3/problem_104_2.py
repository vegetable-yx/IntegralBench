import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for arcsine
x = mp.mpf(1)/4

# Compute arcsine using mpmath's asin function
result = mp.asin(x)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))