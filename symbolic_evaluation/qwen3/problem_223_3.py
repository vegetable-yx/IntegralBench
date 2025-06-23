import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi_value
pi_squared = pi_value ** 2

# Divide by 2 to get the final result
result = pi_squared / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))