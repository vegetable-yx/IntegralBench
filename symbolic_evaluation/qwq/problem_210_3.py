import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute pi using mpmath's constant
pi_value = mp.pi

# Calculate pi cubed
pi_cubed = pi_value ** 3

# Divide by 16 to get the final result
result = pi_cubed / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))