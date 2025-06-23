import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel functions
J1_1 = mp.besselj(1, 1)  # J_1(1) calculation
J0_1 = mp.besselj(0, 1)  # J_0(1) calculation

# Compute terms separately
term1 = (3 * mp.pi / 2) * J1_1  # First term (3π/2)J₁(1)
term2 = (mp.mpf(1)/3) * J0_1    # Second term (1/3)J₀(1)

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))