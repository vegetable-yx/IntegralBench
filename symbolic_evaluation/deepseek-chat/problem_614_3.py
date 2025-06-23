import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the constant value 1/2
result = mp.mpf(1)/2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))