import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_argument = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_value = mp.log(log_argument)

# Multiply by pi to get final result
result = mp.pi * log_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))