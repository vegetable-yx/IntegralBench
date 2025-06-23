import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute the constant pi/2 using mpmath's pi constant
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))