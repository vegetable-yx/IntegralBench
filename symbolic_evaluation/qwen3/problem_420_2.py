import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the first part of the expression: (3 - sqrt(5))/2
sqrt5 = mp.sqrt(5)
part1 = (3 - sqrt5) / 2

# Compute the logarithmic part: 0.5 * ln((sqrt(5) - 1)/2)
numerator = sqrt5 - 1
argument = numerator / 2
log_term = mp.log(argument)
part2 = 0.5 * log_term

# Combine both parts to get the final result
result = part1 - part2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))