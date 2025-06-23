import mpmath as mp
mp.dps = 15

# Calculate each term separately
pi_term = mp.pi / 24
sqrt_term = mp.sqrt(3) / 16

# Combine terms to get final result
result = pi_term - sqrt_term

# Output the result with 10 decimal places
print(mp.nstr(result, n=10))