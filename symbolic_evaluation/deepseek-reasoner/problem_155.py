import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi constant using mpmath's built-in value
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide by 16 to get the final result
result = pi_squared / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))