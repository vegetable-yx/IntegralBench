import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate ln(2) using mpmath's log function
ln2 = mp.log(2)

# Compute the logarithmic term: (1/4) * ln(2)
log_term = (1/4) * ln2

# Compute the pi term: π/8
pi_term = mp.pi / 8

# Combine the components: 2 - log_term + pi_term
result = 2 - log_term + pi_term

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))