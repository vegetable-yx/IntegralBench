import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Cube the pi value
pi_cubed = pi_value ** 3

# Divide the cubed pi by 16
result = pi_cubed / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))