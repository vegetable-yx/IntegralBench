import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the analytical result (constant 0)
result = mp.mpf(0)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))