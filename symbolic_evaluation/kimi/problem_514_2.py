import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate first term: π/6
term1 = mp.pi / 6

# Calculate second term: sqrt(3)/8
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Combine terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))