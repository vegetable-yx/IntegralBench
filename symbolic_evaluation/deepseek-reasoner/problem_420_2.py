import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(5) once and reuse
sqrt5 = mp.sqrt(5)

# Compute the first term (3 - sqrt(5))/2
part1 = (3 - sqrt5) / 2

# Compute the logarithm argument (sqrt(5) - 1)/2
log_arg = (sqrt5 - 1) / 2

# Calculate the logarithmic term (1/2)*ln(log_arg)
part2 = 0.5 * mp.log(log_arg)

# Combine both parts for final result
result = part1 - part2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))