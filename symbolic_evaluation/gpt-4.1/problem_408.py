import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the natural logarithm of (5/3)
log_term = mp.log(5/3)

# Compute the constant fraction 3/5
fraction_term = mp.mpf(3)/5

# Combine the terms: log_term + fraction_term - 1
combined = log_term + fraction_term - 1

# Multiply by 1/8
result = combined / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))