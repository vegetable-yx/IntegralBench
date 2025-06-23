import mpmath as mp
mp.dps = 15

# Calculate Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Compute squared value of Bessel function
j0_sq = j0_1**2

# Calculate the integral term using known identity
integral_term = (mp.pi/2) * j0_sq

# Compute π/4 component
pi_quarter = mp.pi/4

# Combine components for final result
result = pi_quarter - 0.5 * integral_term

print(mp.nstr(result, n=10))