import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Square the pi value
pi_squared = pi_value ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))