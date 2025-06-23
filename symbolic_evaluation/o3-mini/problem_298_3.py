import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4) and square it
gamma_val = mp.gamma(mp.mpf(1)/4)
gamma_sq = gamma_val**2

# Calculate denominator: 8 * sqrt(2 * pi)
denominator = 8 * mp.sqrt(2 * mp.pi)

# Compute the two hypergeometric functions
# First: hyp1 = _2F_1(-1/2, 1/4; 3/4; 1/4)
hyp1 = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.25'), mp.mpf('0.75'), mp.mpf('0.25'))

# Second: hyp2 = _2F_1(1/2, 1/4; 3/4; 1/4)
hyp2 = mp.hyp2f1(mp.mpf('0.5'), mp.mpf('0.25'), mp.mpf('0.75'), mp.mpf('0.25'))

# Compute the expression inside the brackets: 2 * hyp1 - hyp2
bracket_expr = 2 * hyp1 - hyp2

# Combine all parts: (gamma_sq / denominator) * bracket_expr
result = (gamma_sq / denominator) * bracket_expr

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))