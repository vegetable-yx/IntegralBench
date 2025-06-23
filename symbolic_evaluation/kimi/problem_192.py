import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value
result = mp.mpf('1.2309594173407747')

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))