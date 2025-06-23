import mpmath as mp
mp.dps = 15

# Calculate π^2 using mpmath's pi constant
pi_squared = mp.pi ** 2

# Compute π^2/16
term1 = pi_squared / 16

# Calculate 1/4 using precise floating point
term2 = mp.mpf(1)/4

# Subtract the terms to get final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))