import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 192 to get the result
result = pi_cubed / 192

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))