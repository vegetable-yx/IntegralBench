import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Cube the π value
pi_cubed = pi_value ** 3

# Divide by 48 to get the final result
result = pi_cubed / 48

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))