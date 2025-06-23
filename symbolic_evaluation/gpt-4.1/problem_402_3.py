import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π
pi_val = mp.pi

# Divide π by 3
fraction = pi_val / 3

# Take the natural logarithm of (π/3)
log_val = mp.log(fraction)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))