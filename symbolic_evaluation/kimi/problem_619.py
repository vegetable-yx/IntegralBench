import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Get the constant pi
pi_val = mp.pi

# Square pi: π²
pi_squared = mp.power(pi_val, 2)

# Divide by 8: π²/8
result = pi_squared / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))