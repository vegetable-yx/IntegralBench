import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi squared
pi_squared = mp.power(pi_value, 2)

# Compute pi to the fourth power by squaring pi_squared
pi_fourth = mp.power(pi_squared, 2)

# Calculate the final result by dividing pi^4 by 160
result = mp.fdiv(pi_fourth, 160)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))