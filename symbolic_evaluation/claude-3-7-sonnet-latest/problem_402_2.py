import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Calculate the fraction π/3
fraction = pi_val / 3

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))