import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Compute Bessel functions of the first kind
J0_1 = mp.besselj(0, 1)  # J_0(1)
J1_1 = mp.besselj(1, 1)  # J_1(1)

# Compute Struve functions (Hankel type)
H0_1 = mp.struveh(0, 1)  # H_0(1)
H1_1 = mp.struveh(1, 1)  # H_1(1)

# Calculate the inner bracket components
inner_bracket = J1_1 * H0_1 - J0_1 * H1_1

# Compute π/2 multiplier for the inner bracket
pi_over_2 = mp.pi / 2
inner_term = pi_over_2 * inner_bracket

# Combine terms and multiply by π/2
total_expression = J0_1 + inner_term
result = pi_over_2 * total_expression

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))