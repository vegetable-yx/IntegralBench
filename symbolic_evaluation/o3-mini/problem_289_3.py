import mpmath as mp

# Set internal precision
mp.dps = 15

# Define the value of a (user can modify this as needed)
a_val = 1.0
a = mp.mpf(a_val)

# Calculate common expression a^2/4
a_sq_over_4 = a**2 / 4

# Compute gamma function ratios
gamma_ratio1 = mp.gamma(3/4) / mp.gamma(5/4)
gamma_ratio2 = mp.gamma(5/4) / mp.gamma(7/4)

# Evaluate hypergeometric functions
hyp1 = mp.hyp1f2(0.5, 3/4, 3/2, a_sq_over_4)  # _1F_2(1/2; 3/4, 3/2; a^2/4)
hyp2 = mp.hyp1f2(1, 5/4, 3/2, a_sq_over_4)    # _1F_2(1; 5/4, 3/2; a^2/4)

# Compute the two main terms
term1 = gamma_ratio1 * (a/2) * hyp1
term2 = gamma_ratio2 * (a/2)**2 * hyp2

# Combine terms and apply outer factor
bracket = term1 - term2
result = (mp.sqrt(mp.pi) / 4) * bracket

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))