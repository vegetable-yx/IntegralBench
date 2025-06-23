import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = pi_value ** 2

# Divide by 16 to get the final result
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))