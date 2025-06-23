import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared divided by 16
pi_squared = mp.pi ** 2
term1 = pi_squared / 16

# Calculate the logarithm term: ln(1 + sqrt(2))
log_arg = 1 + mp.sqrt(2)
log_val = mp.log(log_arg)

# Square the logarithm and divide by 2
term2 = (log_val ** 2) / 2

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))