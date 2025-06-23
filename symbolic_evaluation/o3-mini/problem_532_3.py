import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Retrieve the mathematical constant π
pi_val = mp.pi

# Square π to obtain the result π²
result = pi_val ** 2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))