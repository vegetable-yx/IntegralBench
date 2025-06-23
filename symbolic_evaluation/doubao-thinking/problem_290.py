import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute K_0(1) - modified Bessel function of the second kind, order 0
k0_val = mp.besselk(0, 1)

# Compute K_1(1) - modified Bessel function of the second kind, order 1
k1_val = mp.besselk(1, 1)

# Calculate the terms: 4 * K_0(1) and 8 * K_1(1)
term1 = 4 * k0_val
term2 = 8 * k1_val

# Combine all terms: 4K_0(1) + 8K_1(1) - 6
result = term1 + term2 - 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))