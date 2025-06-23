import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute natural logarithm of 3
result = mp.log(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))