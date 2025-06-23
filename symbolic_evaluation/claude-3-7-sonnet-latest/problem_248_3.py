import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the first term: π/(4√5)
sqrt5 = mp.sqrt(5)  # Calculate √5
first_term = mp.pi / (4 * sqrt5)

# Compute the argument for the logarithm: (3 + √5)/2
log_arg = (3 + sqrt5) / 2

# Compute the logarithm: ln((3 + √5)/2)
log_val = mp.log(log_arg)

# Compute the second term: (π/8) * ln((3 + √5)/2)
second_term = (mp.pi / 8) * log_val

# Final result: first_term - second_term
result = first_term - second_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))