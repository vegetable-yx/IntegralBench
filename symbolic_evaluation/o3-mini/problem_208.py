import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define fundamental constants
pi = mp.pi
ln2 = mp.ln(2)

# Compute polylogarithm terms
Li2_half = mp.polylog(2, 0.5)  # Dilogarithm at 1/2
Li3_half = mp.polylog(3, 0.5)  # Trilogarithm at 1/2

# Calculate intermediate terms for the numerator
inner_expr = pi**2 - 8 * (ln2**2)  # π² - 8(ln²2)
term1 = 3 * pi * inner_expr * ln2   # 3π(π² - 8ln²2)ln2
term2 = 12 * Li3_half               # 12 Li₃(1/2)
term3 = -12 * ln2 * Li2_half        # -12 ln2 Li₂(1/2)
term4 = -pi**3                      # -π³

# Combine terms for the numerator
numerator = term1 + term2 + term3 + term4

# Final result by dividing by 192
result = numerator / 192

# Output result to exactly 10 decimal places
print(mp.nstr(result, n=10))