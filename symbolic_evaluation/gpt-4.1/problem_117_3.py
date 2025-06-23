import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi to the current precision
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Multiply pi cubed by 5
numerator = 5 * pi_cubed

# Divide the result by 16
result = numerator / 16

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))