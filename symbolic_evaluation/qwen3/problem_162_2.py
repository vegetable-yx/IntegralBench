import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the modified Bessel function of first kind (order 0) at 1
bessel_i0 = mp.besseli(0, 1)

# Multiply all components: π * √2 * I₀(1)
result = mp.pi * sqrt_2 * bessel_i0

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))