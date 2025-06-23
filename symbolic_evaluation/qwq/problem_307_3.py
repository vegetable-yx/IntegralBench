import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate ln(1 + sqrt(2))
log_term = mp.log(1 + sqrt2)

# Multiply by pi
pi_times_log = mp.pi * log_term

# Compute the second part 2*(sqrt(2) - 1)
second_part = 2 * (sqrt2 - 1)

# Sum both components for final result
result = pi_times_log + second_part

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))