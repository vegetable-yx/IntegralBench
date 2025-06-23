import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi)
pi_val = mp.pi

# Compute √2 (square root of 2)
sqrt2 = mp.sqrt(2)

# Compute ln(1 + √2)
log_val = mp.log(1 + sqrt2)

# Compute term1: π²/8
term1 = (pi_val ** 2) / 8

# Compute term2: (π/4) * ln(1 + √2)
term2 = (pi_val / 4) * log_val

# Final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))