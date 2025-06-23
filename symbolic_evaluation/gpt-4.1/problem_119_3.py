import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute pi^3
pi_cubed = mp.pi ** 3

# Divide by 32
result = pi_cubed / 32

# Print result to 10 decimal places
print(mp.nstr(result, n=10))