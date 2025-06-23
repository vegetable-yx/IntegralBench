import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Catalan constant (G)
catalan_constant = mp.catalan

# Apply the negative sign to get the result
result = -catalan_constant

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))