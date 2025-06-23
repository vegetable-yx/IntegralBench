import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Divide pi by 3
fraction = pi_value / 3

# Compute the natural logarithm of the fraction
log_value = mp.log(fraction)

# Multiply the logarithm by 2
result = 2 * log_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))