import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Compute pi to the third power
pi_cubed = mp.pi ** 3

# Divide the result by 8
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))