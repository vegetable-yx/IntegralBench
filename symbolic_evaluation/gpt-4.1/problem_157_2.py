import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the upper incomplete gamma functions for each term
# Γ(5/2, 0.25) - upper incomplete gamma
gamma1 = mp.gammainc(5/2, 0.25, mp.inf)

# Γ(7/2, 0.25) - upper incomplete gamma
gamma2 = mp.gammainc(7/2, 0.25, mp.inf)

# Γ(9/2, 0.25) - upper incomplete gamma
gamma3 = mp.gammainc(9/2, 0.25, mp.inf)

# Calculate the expression inside the brackets: 656*gamma1 - 1152*gamma2 + 256*gamma3
bracket_expr = 656 * gamma1 - 1152 * gamma2 + 256 * gamma3

# Multiply by the exponential factor e^(-0.25)
result = mp.exp(-0.25) * bracket_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))