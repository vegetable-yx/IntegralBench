import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define frequently used constants
sqrt2 = mp.sqrt(2)  # √2
pi_sq = mp.pi**2    # π²

# Compute ln(1 + √2)
log_val = mp.log(1 + sqrt2)

# Compute the terms of the numerator
term1 = -8 * sqrt2 * log_val**3
term2 = 4 * (pi_sq - 6) * log_val**2
term3 = 8 * sqrt2 * (pi_sq - 6) * log_val
term4 = -pi_sq * (pi_sq - 12)

# Compute the dilogarithm terms
dilog_arg1 = 1 - sqrt2  # Argument for Li₂(1 - √2)
dilog_arg2 = sqrt2 - 1   # Argument for Li₂(√2 - 1) = Li₂(1/(1+√2))
term5 = 24 * mp.polylog(2, dilog_arg1)
term6 = 48 * mp.polylog(2, dilog_arg2)

# Sum all terms to get the numerator
numerator = term1 + term2 + term3 + term4 + term5 + term6

# Divide by 48 to get the final result
result = numerator / 48

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))