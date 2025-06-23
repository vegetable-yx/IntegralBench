import mpmath as mp
mp.dps = 15

# Calculate pi constant
pi_value = mp.pi

# Square the value of pi
pi_squared = pi_value ** 2

# Divide the squared pi by 4
result = pi_squared / 4

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))