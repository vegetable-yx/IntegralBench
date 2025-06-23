import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_val = mp.log(one_plus_sqrt2)

# Multiply by pi/2
result = (mp.pi / 2) * log_val

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))