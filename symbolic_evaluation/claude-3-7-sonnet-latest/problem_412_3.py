import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the mathematical constant e
result = mp.e

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))