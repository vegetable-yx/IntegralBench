import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the pi value
pi_squared = mp.power(pi_val, 2)

# Divide by 2 to get final result
result = mp.fdiv(pi_squared, 2)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))