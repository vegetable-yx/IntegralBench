import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate first term: π³/32
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 32

# Calculate components for second term: (π/8) * ln²(1 + √2)
sqrt2 = mp.sqrt(2)
log_argument = 1 + sqrt2
log_value = mp.log(log_argument)
log_squared = log_value ** 2
term2 = (mp.pi / 8) * log_squared

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))