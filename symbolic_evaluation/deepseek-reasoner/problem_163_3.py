import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Multiply by 2 to get final result
result = 2 * pi_cubed

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))