import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Square the pi value
pi_squared = pi_val ** 2

# Divide the squared pi by 4
result = pi_squared / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))