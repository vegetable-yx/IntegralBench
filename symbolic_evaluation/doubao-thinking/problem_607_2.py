import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by logarithm term and divide by 2
result = (mp.pi / 2) * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))