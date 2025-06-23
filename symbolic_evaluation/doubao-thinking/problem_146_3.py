import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Divide by 2 to get the final result
result = mp.fdiv(pi_squared, 2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))