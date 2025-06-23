import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Calculate the argument of the logarithm: (sqrt(3) + 1) / (sqrt(3) - 1)
log_arg = (sqrt3 + 1) / (sqrt3 - 1)

# Compute the natural logarithm of the argument
log_term = mp.log(log_arg)

# Calculate the term: 27 * sqrt(3) * log_term
term = 27 * sqrt3 * log_term

# Compute the numerator: 72*pi - 128 - term
numerator = 72 * mp.pi - 128 - term

# Divide the numerator by 384 to get the result
result = numerator / 384

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))