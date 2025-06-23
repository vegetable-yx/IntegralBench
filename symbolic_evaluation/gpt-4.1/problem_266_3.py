import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate each component separately
pi_term = -mp.pi / 2  # First term: -π/2
bessel_term = mp.besselj(0, 2)  # Bessel function J₀(2)

# Combine terms for final result
result = pi_term + bessel_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))