import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Square the pi_value
pi_squared = mp.power(pi_value, 2)

# Divide the squared pi by 8
result = mp.fdiv(pi_squared, 8)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))