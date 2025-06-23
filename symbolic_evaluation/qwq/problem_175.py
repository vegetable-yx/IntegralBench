import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 80 to get the final result
result = pi_cubed / 80

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))