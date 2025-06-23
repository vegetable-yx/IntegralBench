import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the natural logarithm of 3
result = mp.log(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))