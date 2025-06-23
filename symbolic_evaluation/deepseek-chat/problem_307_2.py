import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 4 to get the result
result = pi_squared / 4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))