import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural logarithm of 3
result = mp.log(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))