import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
pi_squared = pi_value ** 2

# Divide by 2 to obtain the final result
result = pi_squared / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))