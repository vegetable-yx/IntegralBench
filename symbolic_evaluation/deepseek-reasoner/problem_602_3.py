import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi^4 by squaring pi twice
pi_squared = pi_val ** 2
pi_power4 = pi_squared ** 2

# Divide by 120 to get the final result
result = pi_power4 / 120

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))