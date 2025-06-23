import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute natural logarithm of 3 using mpmath's log function
result = mp.log(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))