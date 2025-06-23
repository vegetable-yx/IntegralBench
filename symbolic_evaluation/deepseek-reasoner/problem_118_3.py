import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 4 to get final result
result = mp.fdiv(pi_squared, 4)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))