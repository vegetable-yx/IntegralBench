import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide by 8 to get final result
result = pi_squared / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))