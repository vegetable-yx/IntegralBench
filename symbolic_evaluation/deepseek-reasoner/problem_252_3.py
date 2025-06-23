import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2) using mpmath's square root function
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by pi constant from mpmath
result = mp.pi * log_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))