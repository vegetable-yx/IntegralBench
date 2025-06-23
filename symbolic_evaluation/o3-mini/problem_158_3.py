import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is the constant 1
result = mp.mpf(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))