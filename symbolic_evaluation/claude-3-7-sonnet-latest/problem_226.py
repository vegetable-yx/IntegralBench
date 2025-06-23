import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument: 1 + sqrt(2)
arg = 1 + sqrt2

# Calculate the natural logarithm of the argument
log_val = mp.log(arg)

# Square the logarithm
log_sq = log_val ** 2

# Multiply by pi to get the final result
result = mp.pi * log_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))