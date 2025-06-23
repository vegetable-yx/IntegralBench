import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π²/32 term
pi_squared = mp.pi ** 2
term1 = pi_squared / 32

# Calculate (ln(1+√2))²/4 term
sqrt2 = mp.sqrt(2)
log_argument = 1 + sqrt2
log_value = mp.log(log_argument)
squared_log = log_value ** 2
term2 = squared_log / 4

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))