import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: 1 + sqrt(2)
inner_log = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_log)

# Multiply the logarithm by pi
result = mp.pi * log_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))