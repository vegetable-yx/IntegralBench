import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the square root of 2
sqrt_val = mp.sqrt(2)

# Add 1 to the square root of 2
sum_val = 1 + sqrt_val

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(sum_val)

# Multiply by π/2
result = (mp.pi / 2) * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))