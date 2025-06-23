import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: 2 + sqrt(5)
log_arg = 2 + sqrt5

# Compute the natural logarithm of (2 + sqrt(5))
log_val = mp.log(log_arg)

# Square the logarithm
log_squared = log_val ** 2

# Multiply by pi and divide by 8
result = (mp.pi / 8) * log_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))