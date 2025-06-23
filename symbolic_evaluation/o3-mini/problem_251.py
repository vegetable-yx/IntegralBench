import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (sqrt(2) + 1) / (sqrt(2) - 1)
log_arg = (sqrt2 + 1) / (sqrt2 - 1)

# Compute the logarithmic term: ln((sqrt(2)+1)/(sqrt(2)-1))
log_term = mp.log(log_arg)

# Calculate the prefactor: (pi/2) multiplied by the logarithmic term
pi_term = (mp.pi / 2) * log_term

# Compute the base value: (sqrt(2) - 1)
base_val = sqrt2 - 1

# Square the base value for the dilogarithm arguments
t_squared = base_val**2

# Compute the two dilogarithm terms:
#   Li2(-t_squared) and Li2(t_squared)
dilog_term1 = mp.polylog(2, -t_squared)
dilog_term2 = mp.polylog(2, t_squared)

# Combine all terms: pi_term + dilog_term1 - dilog_term2
result = pi_term + dilog_term1 - dilog_term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))