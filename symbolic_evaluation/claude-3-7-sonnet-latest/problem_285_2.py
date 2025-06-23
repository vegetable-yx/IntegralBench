import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute π²
pi_squared = mp.power(mp.pi, 2)

# Compute π²/32
term1 = pi_squared / 32

# Compute ln(1 + √2)
log_arg = 1 + mp.sqrt(2)
log_term = mp.log(log_arg)

# Compute π * ln(1 + √2)
pi_log = mp.pi * log_term

# Compute π * ln(1 + √2) / 8
term2 = pi_log / 8

# Final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))