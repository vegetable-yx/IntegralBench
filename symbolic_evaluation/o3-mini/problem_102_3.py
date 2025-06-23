import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate components
sqrt3 = mp.sqrt(3)  # Square root of 3

# Compute the argument of the logarithm: (sqrt(3) + 1) / (sqrt(3) - 1)
log_arg = (sqrt3 + 1) / (sqrt3 - 1)

# Calculate the natural logarithm of the argument
log_term = mp.log(log_arg)

# Compute the factor: (sqrt(3) - 4) * log_term
factor = (sqrt3 - 4) * log_term

# Compute 2 * pi
two_pi = 2 * mp.pi

# Sum: 2*pi + factor
numerator = two_pi + factor

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))