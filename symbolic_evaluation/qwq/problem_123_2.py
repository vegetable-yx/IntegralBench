import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
pi_squared = pi_value ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))