import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Compute 2 * pi
two_pi = 2 * pi_val

# Compute pi squared
pi_squared = pi_val ** 2

# Divide pi squared by 2
pi_sq_div_2 = pi_squared / 2

# Subtract (pi squared / 2) from (2 * pi)
result = two_pi - pi_sq_div_2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))