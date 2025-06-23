import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural logarithm of 2
result = mp.log(2)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))