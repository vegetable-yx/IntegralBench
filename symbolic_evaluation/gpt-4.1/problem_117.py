import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi from mpmath constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Multiply by 11
numerator = 11 * pi_cubed

# Divide by 256
result = numerator / 256

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))