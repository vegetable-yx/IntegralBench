import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel functions
J0_2 = mp.besselj(0, 2)  # J_0(2)
J1_2 = mp.besselj(1, 2)  # J_1(2)

# Calculate the expression components
term_1 = 1
term_2 = -2 * J0_2
term_3 = J1_2

# Combine terms and multiply by π/4
combined_terms = term_1 + term_2 + term_3
result = (mp.pi / 4) * combined_terms

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))