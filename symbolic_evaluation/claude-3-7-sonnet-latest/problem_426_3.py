import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is a constant value
result = mp.mpf(2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))