import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the first part: (3 - sqrt(5)) / 2
part1 = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (sqrt(5) - 1) / 2
log_arg = (sqrt5 - 1) / 2

# Calculate the natural logarithm of the argument
log_term = mp.log(log_arg)

# Compute the second part: (1/2) * log_term
part2 = 0.5 * log_term

# Combine the parts to get the final result
result = part1 - part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))