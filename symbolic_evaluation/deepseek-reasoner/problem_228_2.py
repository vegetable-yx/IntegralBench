import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate first term: π²/16
pi_squared = mp.pi ** 2
term1 = pi_squared / 16

# Calculate logarithmic term components
sqrt2 = mp.sqrt(2)          # Compute √2
log_argument = 1 + sqrt2    # Argument for natural logarithm
log_value = mp.log(log_argument)  # ln(1+√2)
squared_log = log_value ** 2  # (ln(1+√2))²
term2 = 0.5 * squared_log    # ½(ln(1+√2))²

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))