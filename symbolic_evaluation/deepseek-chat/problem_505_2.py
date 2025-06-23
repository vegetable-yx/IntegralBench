import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute π/4 using mpmath's pi constant
result = mp.pi / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))