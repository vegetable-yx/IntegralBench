import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is a constant: 99
result = mp.mpf(99)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))