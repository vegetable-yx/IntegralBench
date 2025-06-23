import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute arcsin(1/4) component
arcsin_val = mp.asin(mp.mpf(1)/4)

# Compute pi/8 * arcsin(1/4)
term1 = (mp.pi / 8) * arcsin_val

# Compute sqrt(15) component
sqrt15 = mp.sqrt(15)

# Compute log argument (1 + sqrt(15))/4
log_arg = (mp.mpf(1) + sqrt15) / 4

# Compute logarithmic term
log_term = mp.log(log_arg)

# Combine terms for second part: (sqrt(15)/16) * log_term
term2 = (sqrt15 / 16) * log_term

# Sum both terms for final result
result = term1 + term2

# Print with 10 decimal precision
print(mp.nstr(result, n=10))