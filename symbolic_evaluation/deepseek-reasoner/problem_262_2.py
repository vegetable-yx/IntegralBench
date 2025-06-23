import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the numerator (1 + sqrt(2))
numerator = 1 + sqrt_2

# Calculate the argument for the logarithm: (1 + sqrt(2))/2
log_argument = numerator / 2

# Compute the natural logarithm of the argument
log_value = mp.log(log_argument)

# Calculate π/2
pi_over_2 = mp.pi / 2

# Multiply π/2 with the logarithm value to get final result
result = pi_over_2 * log_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))