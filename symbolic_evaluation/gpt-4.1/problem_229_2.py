import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 120 to get the final result
result = pi_cubed / 120

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))