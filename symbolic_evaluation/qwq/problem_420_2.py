import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(5) once for reuse
sqrt5 = mp.sqrt(5)

# Compute first term: (3 - sqrt(5))/2
first_part = (3 - sqrt5) / 2

# Compute the argument: (sqrt(5) - 1)/2
log_argument = (sqrt5 - 1) / 2

# Compute second term: 0.5 * ln((sqrt(5)-1)/2)
second_part = 0.5 * mp.log(log_argument)

# Combine both parts for final result
result = first_part - second_part

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))