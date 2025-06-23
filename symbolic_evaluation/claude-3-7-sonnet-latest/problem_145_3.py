import mpmath as mp

# Set the internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Compute pi/4 using mpmath's pi constant
result = mp.pi / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))