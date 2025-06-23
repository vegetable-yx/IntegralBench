import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate π³ component
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 144

# Calculate logarithmic component
log_term = mp.log(mp.mpf(4)/3)  # Compute ln(4/3) with high precision
term2 = (mp.pi * log_term) / 12

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))