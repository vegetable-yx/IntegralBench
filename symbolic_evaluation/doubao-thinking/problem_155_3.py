import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 16 to get final result
result = pi_squared / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))