import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant square root of 2
sqrt2 = mp.sqrt(2)

# Compute the first term: π / √2
term1 = mp.pi / sqrt2

# Compute the second term: π / 2
term2 = mp.pi / 2

# Compute the argument for the logarithm: (1 + √2) / 2
log_arg = (1 + sqrt2) / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute the third term: (π / 4) * ln((1 + √2) / 2)
term3 = (mp.pi / 4) * log_val

# Combine all terms: term1 - term2 - term3
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))