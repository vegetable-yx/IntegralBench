import mpmath as mp
mp.dps = 15  # Set internal precision

# Compute Bessel J functions at z=1
J0_1 = mp.besselj(0, 1)
J1_1 = mp.besselj(1, 1)

# Compute Struve H functions at z=1
H0_1 = mp.struveh(0, 1)
H1_1 = mp.struveh(1, 1)

# Calculate the integral of J0(z) from 0 to 1 using closed-form expression
integral_J0 = J0_1 + (mp.pi/2) * (J1_1 * H0_1 - J0_1 * H1_1)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * integral_J0

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))