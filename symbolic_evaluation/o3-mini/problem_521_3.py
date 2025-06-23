import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute natural logarithm of 3
result = mp.log(3)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))