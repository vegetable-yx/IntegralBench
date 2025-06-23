import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide the result by 24
result = pi_cubed / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))