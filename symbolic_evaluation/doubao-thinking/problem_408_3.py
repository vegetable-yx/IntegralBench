import mpmath as mp
mp.dps = 15  # Set internal decimal places for high precision

# Calculate the natural logarithm term
fraction = mp.mpf(5)/3  # Compute 5/3 with mpmath precision
log_term = mp.log(fraction)  # Calculate ln(5/3)

# Compute the first part of the expression
log_part = log_term / 8  # Divide logarithm result by 8

# Calculate the second part of the expression
constant_part = mp.mpf(1)/20  # Compute 1/20 with mpmath precision

# Combine both parts for final result
result = log_part - constant_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))