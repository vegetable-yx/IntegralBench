import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sqrt(2) for later use
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_argument = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
ln_term = mp.log(log_argument)

# Compute the first part of the expression: π * (ln_term)/2
pi_times_log_part = (mp.pi * ln_term) / 2

# Final result: subtract sqrt2 from the computed part
result = pi_times_log_part - sqrt2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))