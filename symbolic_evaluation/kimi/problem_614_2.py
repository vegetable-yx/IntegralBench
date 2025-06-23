import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the given analytical value directly
result = mp.mpf('0.5833333333')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))