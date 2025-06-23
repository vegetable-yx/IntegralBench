import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate first term: π * ln(1 + √2)
sqrt2 = mp.sqrt(2)
log_term = mp.log(1 + sqrt2)
pi_term = mp.pi
term1 = pi_term * log_term

# Calculate second term: 2*(√2 - 1)
term2 = 2 * (sqrt2 - 1)

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))