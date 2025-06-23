import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute pi to high precision using mpmath constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide the result by 16
result = pi_cubed / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))