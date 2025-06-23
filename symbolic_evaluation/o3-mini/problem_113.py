import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Compute gamma(1/4) and its square
gamma_14 = mp.gamma(1/4)
gamma_14_sq = gamma_14 * gamma_14

# Compute the constant factor: Gamma(1/4)^2 / (8 * sqrt(pi))
denominator = 8 * mp.sqrt(mp.pi)
constant_factor = gamma_14_sq / denominator

# Compute the hypergeometric function: _3F_2(1/2, 1, 1; 3/4, 5/4; 1/4)
hyp_val = mp.hyper([0.5, 1, 1], [0.75, 1.25], 0.25)

# Compute 4 * ln(2)
four_ln2 = 4 * mp.log(2)

# Compute the expression inside the brackets: 4*ln(2) - hyp_val
bracket = four_ln2 - hyp_val

# Multiply constant_factor by bracket to get the final result
result = constant_factor * bracket

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))