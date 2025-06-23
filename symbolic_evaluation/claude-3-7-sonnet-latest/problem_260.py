import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Euler's constant (γ)
gamma = mp.euler

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Sum γ and ln(2)
gamma_plus_ln2 = gamma + ln2

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute Bessel function J0 at 1
bessel_j0_1 = mp.besselj(0, 1)

# Multiply the components: (π/2) * J0(1) * (γ + ln(2))
result = pi_over_2 * bessel_j0_1 * gamma_plus_ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))