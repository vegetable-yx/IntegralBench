import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute pi
pi_val = mp.pi

# Compute the term (1 - pi/2)
term = 1 - (pi_val / 2)

# Multiply the components: sqrt(2) * pi * (1 - pi/2)
result = sqrt2 * pi_val * term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))