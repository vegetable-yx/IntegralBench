import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate intermediate values
# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (1 + sqrt(2)) / 2
log_arg = (1 + sqrt2) / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute each term:
term1 = mp.pi / sqrt2          # π / √2
term2 = mp.pi / 2              # π/2
term3 = (mp.pi / 2) * log_val  # (π/2) * ln((1+√2)/2)

# Combine the terms: term1 - term2 - term3
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))