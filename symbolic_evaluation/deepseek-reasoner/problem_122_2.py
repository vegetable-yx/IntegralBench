import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 4 to get final result
result = pi_squared / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))