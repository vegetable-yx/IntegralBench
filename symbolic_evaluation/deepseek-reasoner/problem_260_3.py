import mpmath as mp
mp.dps = 15

# Calculate Bessel functions at t=1
J0_1 = mp.besselj(0, 1)
J1_1 = mp.besselj(1, 1)

# Calculate Struve functions at t=1
H0_1 = mp.struveh(0, 1)
H1_1 = mp.struveh(1, 1)

# Compute the integral components using analytical formula
integral_term1 = J0_1  # From the x*J0(x) term at x=1
integral_term2 = (mp.pi/2) * (J1_1 * H0_1 - J0_1 * H1_1)  # Struve function terms

# Combine terms to get the integral_{0}^{1} J0(t) dt
integral_value = integral_term1 + integral_term2

# Multiply by π/2 for final result
result = (mp.pi / 2) * integral_value

print(mp.nstr(result, n=10))