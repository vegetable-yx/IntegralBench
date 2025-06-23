import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is given as a constant value
result = mp.mpf('4.1887902047863905')

# Print the result with exactly 10 significant digits
print(mp.nstr(result, n=10))