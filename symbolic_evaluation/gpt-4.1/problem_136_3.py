import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the constant 2
result = mp.mpf(2)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))