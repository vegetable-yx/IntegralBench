import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 6 to get the result
result = pi_squared / 6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))