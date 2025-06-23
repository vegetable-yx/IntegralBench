import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Add 1 to the square root
sqrt2_plus_1 = sqrt2 + 1

# Compute the natural logarithm of (sqrt(2) + 1)
log_term = mp.log(sqrt2_plus_1)

# Multiply by pi/2
result = (mp.pi / 2) * log_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))