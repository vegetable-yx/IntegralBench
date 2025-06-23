import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute the mathematical constant π
pi_value = mp.pi

# Calculate the negative of π
result = -pi_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))