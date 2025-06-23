import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the constant 4
result = mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))