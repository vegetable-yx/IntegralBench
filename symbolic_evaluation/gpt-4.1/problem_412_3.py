import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# The analytical expression is the mathematical constant e
result = mp.e

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))