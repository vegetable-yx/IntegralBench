import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 32 to get the final result
result = pi_cubed / 32

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))