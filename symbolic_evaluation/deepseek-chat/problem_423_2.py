import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical solution is a constant: 99
result = mp.mpf(99)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))