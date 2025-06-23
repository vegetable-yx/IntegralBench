import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel function of the first kind, order 0, at 2
bessel_i0 = mp.besseli(0, 2)

# Calculate the modified Bessel function of the first kind, order 1, at 2
bessel_i1 = mp.besseli(1, 2)

# Compute the first term: (π/8) * I₀(2)
term1 = (mp.pi / 8) * bessel_i0

# Compute the second term: (1/4) * I₁(2)
term2 = (1/4) * bessel_i1

# Combine the terms: π/8 * I₀(2) - 1/4 * I₁(2)
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))