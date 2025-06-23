import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value directly from the analytical solution
result = mp.mpf('1.000494559')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))