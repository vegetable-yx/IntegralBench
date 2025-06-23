import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Square Gamma(1/4)
gamma_sq = gamma_val**2

# Compute denominator: 4 * sqrt(2 * pi)
denom = 4 * mp.sqrt(2 * mp.pi)

# Calculate the hypergeometric function 2F1(1/2, 1/4; 5/4; 1/2)
hyp_val = mp.hyp2f1(0.5, 0.25, 1.25, 0.5)

# Combine all parts: (gamma_sq / denom) * hyp_val
result = (gamma_sq / denom) * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))