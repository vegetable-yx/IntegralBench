import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# The analytical result is exactly zero
result = mp.mpf(0)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))