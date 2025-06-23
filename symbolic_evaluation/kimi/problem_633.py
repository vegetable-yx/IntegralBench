import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical result is exactly zero
result = 0

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))