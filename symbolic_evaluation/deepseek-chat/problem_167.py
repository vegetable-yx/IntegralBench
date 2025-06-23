import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 4 to get the final result
result = pi_squared / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))