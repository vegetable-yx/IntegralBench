import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is infinity
result = mp.inf

# Print the result to 10 decimal places (will output 'inf')
print(mp.nstr(result, n=10))