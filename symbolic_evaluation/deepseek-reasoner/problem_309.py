import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide the squared result by 2
result = mp.fdiv(pi_squared, 2)

# Print the final value with 10 decimal precision
print(mp.nstr(result, n=10))