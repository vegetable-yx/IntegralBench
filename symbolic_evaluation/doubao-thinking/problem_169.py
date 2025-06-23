import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi constant
pi_value = mp.pi

# Square the pi value
pi_squared = pi_value ** 2

# Divide squared pi by 4 to get final result
result = pi_squared / 4

# Print result with 10 decimal places
print(mp.nstr(result, n=10))