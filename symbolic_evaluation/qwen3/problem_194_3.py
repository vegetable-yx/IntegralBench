import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute term_a = π/6 + sqrt(3) - 2
term_a = mp.pi/6 + mp.sqrt(3) - 2

# Compute term_b = (π/2) * term_a
term_b = (mp.pi/2) * term_a

# Compute components for integral I
# I1 calculation: ∫ x arcsin(x)/sqrt(4-x²) dx from 0 to 1
I1_part1 = -(mp.pi/2) * mp.sqrt(3)
E_14 = mp.ellipe(mp.mpf(1)/4)  # E(1/4)
I1 = I1_part1 + 2 * E_14

# I2 calculation: ∫ sqrt(1-x²)/sqrt(4-x²) dx from 0 to 1
E_12 = mp.ellipe(mp.mpf(1)/2)  # E(1/2)
K_12 = mp.ellipk(mp.mpf(1)/2)  # K(1/2)
I2 = 0.5 * E_12 - 1.5 * K_12

# Combine parts to get integral I
I = (mp.pi**2)/12 - (I1 + I2)

# Final result calculation
result = term_a - term_b + I

# Print result with 10 decimal places
print(mp.nstr(result, n=10))