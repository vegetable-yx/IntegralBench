import mpmath as mp

# Set the internal decimal precision to 15 for calculations
mp.dps = 15

# The analytical solution is a constant integer: 1005
result = 1005

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))