import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm
log_argument = 2 + sqrt5

# Calculate the natural logarithm of (2 + sqrt(5))
log_value = mp.log(log_argument)

# Compute π/4
pi_over_4 = mp.pi / 4

# Multiply the components to get the final result
result = pi_over_4 * log_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))