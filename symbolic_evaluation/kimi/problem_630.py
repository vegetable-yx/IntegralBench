import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 3
sqrt3 = mp.sqrt(3)

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Compute π/3
pi_over_3 = mp.pi / 3

# Compute first term: ln(3) * π/3
term1 = ln3 * pi_over_3

# Compute dilogarithm for -√3
Li2_minus_sqrt3 = mp.polylog(2, -sqrt3)

# Compute dilogarithm for -1/√3
Li2_minus_inv_sqrt3 = mp.polylog(2, -1/sqrt3)

# Combine the dilogarithm terms: -Li₂(-√3) + Li₂(-1/√3)
dilog_terms = -Li2_minus_sqrt3 + Li2_minus_inv_sqrt3

# Combine all terms: (ln(3)*π/3) + [-Li₂(-√3) + Li₂(-1/√3)]
numerator = term1 + dilog_terms

# Divide by √3 to get the final result
result = numerator / sqrt3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))