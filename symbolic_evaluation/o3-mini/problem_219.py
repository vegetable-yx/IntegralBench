import mpmath as mp

# Set internal decimal precision to 15 for accuracy
mp.dps = 15

# Calculate constants and function values
pi = mp.pi
sqrt_2pi = mp.sqrt(2 * pi)  # Precompute sqrt(2*pi)

# Compute Bessel functions at order -1/4 and 1/4 evaluated at 1
J_minus_quarter = mp.besselj(-1/4, 1)
J_quarter = mp.besselj(1/4, 1)

# Compute trigonometric constants: cos(pi/8) and sin(pi/8)
pi_over_8 = pi / 8
cos_pi8 = mp.cos(pi_over_8)
sin_pi8 = mp.sin(pi_over_8)

# Compute the terms: J_{-1/4}(1)*cos(π/8) and J_{1/4}(1)*sin(π/8)
term1 = J_minus_quarter * cos_pi8
term2 = J_quarter * sin_pi8

# Combine terms: (term1 - term2)
combined_terms = term1 - term2

# Final result: sqrt(2π) * (term1 - term2)
result = sqrt_2pi * combined_terms

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))