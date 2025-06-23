import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# The analytical expression is pi/2
# Compute pi/2 using mpmath's constant for pi
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))