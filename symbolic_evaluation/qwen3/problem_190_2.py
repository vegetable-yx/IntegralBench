import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ln(1 + sqrt(2)) and square it
sqrt2 = mp.sqrt(2)
log_argument = 1 + sqrt2
log_term = mp.log(log_argument)
log_squared = log_term ** 2

# Calculate π²/12 term
pi_squared = mp.pi ** 2
pi_term = pi_squared / 12

# Compute the difference between squared log term and π² term
difference = log_squared - pi_term

# Multiply by π/64 to get final result
result = (mp.pi / 64) * difference

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))