import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function values
y0_1 = mp.bessely(0, 1)  # Y_0(1)
k0_2 = mp.besselk(0, 2)  # K_0(2)
y0_2 = mp.bessely(0, 2)  # Y_0(2)
k0_1 = mp.besselk(0, 1)  # K_0(1)

# Calculate the numerator: Y_0(1)*K_0(2) - Y_0(2)*K_0(1)
numerator = y0_1 * k0_2 - y0_2 * k0_1

# Calculate the denominator: 2*π
denominator = 2 * mp.pi

# Final result
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))