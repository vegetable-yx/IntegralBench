import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# Compute natural logarithm of 2
result = mp.log(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))