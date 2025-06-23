import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate gamma function values for fractions
gamma_5_4 = mp.gamma(mp.mpf(5)/4)   # Γ(5/4)
gamma_7_4 = mp.gamma(mp.mpf(7)/4)   # Γ(7/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)   # Γ(3/4)

# Compute the inner expression: 2*Γ(7/4) - 3*Γ(3/4)
inner_expr = 2 * gamma_7_4 - 3 * gamma_3_4

# Multiply by 8 and Γ(5/4)
result = 8 * gamma_5_4 * inner_expr

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))