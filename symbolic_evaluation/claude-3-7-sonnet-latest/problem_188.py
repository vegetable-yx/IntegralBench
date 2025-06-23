import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute π/4 using mpmath's pi constant
pi_value = mp.pi
result = pi_value / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))