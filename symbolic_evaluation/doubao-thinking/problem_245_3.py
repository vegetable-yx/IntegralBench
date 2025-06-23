import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi squared
pi_squared = pi_val ** 2

# Multiply by 15 to get the numerator
numerator = 15 * pi_squared

# Divide by 16 to obtain the final result
result = numerator / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))