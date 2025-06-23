import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute (3 - sqrt(5)) / 2
part1 = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (1 + sqrt(5)) / 2
log_arg = (1 + sqrt5) / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply the logarithm by 1/2 to get the second part
part2 = 0.5 * log_val

# Sum the two parts to get the final result
result = part1 + part2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))