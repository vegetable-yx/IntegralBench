import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi from mpmath constant
pi_val = mp.pi

# Compute pi cubed: π^3
pi_cubed = pi_val ** 3

# Divide by 4 to get the result
result = pi_cubed / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))