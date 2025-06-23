import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the first part: (3 + sqrt(5)) / 2
part1 = (3 + sqrt5) / 2

# Compute the argument for the logarithm: (-1 + sqrt(5)) / 2
log_arg = (-1 + sqrt5) / 2

# Compute the logarithm and then the second part: (1/2) * ln(log_arg)
part2 = 0.5 * mp.log(log_arg)

# Combine the two parts to get the final result
result = part1 - part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))