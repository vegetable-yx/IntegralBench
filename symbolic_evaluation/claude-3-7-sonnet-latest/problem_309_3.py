import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Add 1 to the square root of 2
one_plus_sqrt2 = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by 2*pi
result = 2 * mp.pi * log_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))