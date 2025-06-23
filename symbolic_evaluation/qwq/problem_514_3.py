import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/6 term
pi_term = mp.pi / 6

# Calculate sqrt(3)/8 term
sqrt3 = mp.sqrt(3)
sqrt_term = sqrt3 / 8

# Sum both terms for final result
result = pi_term + sqrt_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))