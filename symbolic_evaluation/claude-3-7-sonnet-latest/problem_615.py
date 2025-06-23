import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# The analytical solution is the constant value 14
result = mp.mpf(14)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))