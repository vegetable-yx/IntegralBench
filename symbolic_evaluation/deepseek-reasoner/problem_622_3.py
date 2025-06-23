import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/4 using mpmath's constant
pi_term = mp.pi / 4

# Calculate the constant term 1/2 using high-precision arithmetic
constant_term = mp.mpf(1)/2

# Combine terms to get final result
result = pi_term - constant_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))