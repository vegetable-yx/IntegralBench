import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the natural logarithm of 2
result = mp.log(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))