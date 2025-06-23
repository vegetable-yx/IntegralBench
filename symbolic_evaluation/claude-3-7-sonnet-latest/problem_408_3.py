import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the fraction inside the logarithm: 5/3
fraction = mp.mpf(5) / mp.mpf(3)

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Divide the logarithm by 8
term1 = log_val / mp.mpf(8)

# Compute the constant term: 1/20
term2 = mp.mpf(1) / mp.mpf(20)

# Combine the terms: ln(5/3)/8 - 1/20
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))