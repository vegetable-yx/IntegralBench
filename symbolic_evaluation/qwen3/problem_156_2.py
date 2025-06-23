import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the first term (π²/4)
term1 = pi_squared / 4

# Calculate the argument for the logarithm
sqrt2 = mp.sqrt(2)
log_argument = 1 + sqrt2

# Calculate the logarithmic term
log_term = mp.log(log_argument)

# Combine terms for final result
result = term1 * log_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))