import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π²/12 component
pi_squared_over_12 = mp.pi**2 / 12

# Calculate π/3 component
pi_over_3 = mp.pi / 3

# Calculate sqrt(3)/2 * ln(2 + sqrt(3)) component
sqrt3 = mp.sqrt(3)
log_argument = 2 + sqrt3
ln_term = mp.log(log_argument)
sqrt3_over_2_ln = (sqrt3 / 2) * ln_term

# Combine all components
result = pi_squared_over_12 - pi_over_3 + sqrt3_over_2_ln

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))