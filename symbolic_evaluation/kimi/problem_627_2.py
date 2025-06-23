import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute π/2 using mpmath's pi constant
pi_value = mp.pi
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))