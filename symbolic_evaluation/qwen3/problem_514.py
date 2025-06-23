import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/6 term
term1 = mp.pi / 6

# Calculate sqrt(3)/8 term
term2 = mp.sqrt(3) / 8

# Sum both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))