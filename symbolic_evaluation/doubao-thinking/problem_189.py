import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the numerator (1 + sqrt(5))
numerator = 1 + sqrt5

# Calculate the argument for the logarithm: (1 + sqrt(5))/2
log_argument = numerator / 2

# Compute the natural logarithm of the argument
log_term = mp.log(log_argument)

# Calculate pi/2
pi_half = mp.pi / 2

# Multiply the terms to get the final result
result = pi_half * log_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))