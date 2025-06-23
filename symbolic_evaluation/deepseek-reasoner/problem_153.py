import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's built-in constant
pi_val = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_val, 2)

# Divide by 16 to get the final result
result = pi_squared / 16

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))