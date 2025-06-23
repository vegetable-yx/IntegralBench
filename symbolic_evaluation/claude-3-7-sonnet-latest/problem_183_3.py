import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: 2 + sqrt(5)
log_arg = 2 + sqrt5

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply by pi/2
result = (mp.pi / 2) * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))