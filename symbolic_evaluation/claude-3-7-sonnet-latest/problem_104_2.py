import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute π/6
term1 = mp.pi / 6

# Compute √3
sqrt3 = mp.sqrt(3)

# Compute √3 / 8
term2 = sqrt3 / 8

# Final result: π/6 - √3/8
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))