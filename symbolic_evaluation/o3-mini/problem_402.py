import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Compute the fraction pi/3
fraction = pi_val / 3

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply the logarithm by 2 to get the final result
result = 2 * log_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))