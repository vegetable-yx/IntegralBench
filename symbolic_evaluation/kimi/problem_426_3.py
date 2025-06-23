import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate first term: π/4
pi_over_4 = mp.pi / 4

# Calculate second term: (π * sqrt(3))/9
sqrt3 = mp.sqrt(3)
pi_sqrt3_over_9 = (mp.pi * sqrt3) / 9

# Combine both terms
result = pi_over_4 + pi_sqrt3_over_9

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))