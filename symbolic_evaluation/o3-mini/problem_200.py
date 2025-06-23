import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the argument for Bessel functions: 1/sqrt(2)
arg = 1 / mp.sqrt(2)

# Compute Gamma functions
gamma_1_4 = mp.gamma(1/4)
gamma_3_4 = mp.gamma(3/4)

# Compute Bessel functions of fractional order
J_neg_1_4 = mp.besselj(-1/4, arg)  # J_{-1/4}(1/sqrt(2))
J_pos_1_4 = mp.besselj(1/4, arg)   # J_{1/4}(1/sqrt(2))

# Compute constants: 2^{3/4} and 2^{5/4}
two_power_3_4 = mp.power(2, 3/4)
two_power_5_4 = mp.power(2, 5/4)

# Compute each term in the expression
term1 = gamma_1_4 / two_power_3_4 * J_neg_1_4
term2 = gamma_3_4 / two_power_5_4 * J_pos_1_4

# Combine terms to get final result
result = term1 - term2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))