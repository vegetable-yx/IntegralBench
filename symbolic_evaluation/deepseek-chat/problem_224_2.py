import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val**3

# Divide by 16 to get the result
result = pi_cubed / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))