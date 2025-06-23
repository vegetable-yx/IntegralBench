import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/6 using mpmath's pi constant
pi_term = mp.pi / 6

# Calculate sqrt(3)/8 using mpmath's square root function
sqrt3_over_8 = mp.sqrt(3) / 8

# Sum the two terms to get final result
result = pi_term + sqrt3_over_8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))