import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = pi_val ** 2

# Divide the squared π by 2 to get the result
result = pi_squared / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))