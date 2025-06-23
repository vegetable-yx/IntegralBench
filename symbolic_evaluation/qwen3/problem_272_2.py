import mpmath as mp
mp.dps = 15

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) - 1) term
term1 = sqrt2 - 1

# Calculate argument for logarithm
log_arg = (1 + sqrt2) / 2

# Compute natural logarithm term
log_term = mp.log(log_arg)

# Combine all components
combined = term1 - log_term

# Multiply by pi/2 for final result
result = (mp.pi / 2) * combined

print(mp.nstr(result, n=10))