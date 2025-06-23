import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute gamma values
gamma_14 = mp.gamma(mp.mpf(1)/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute the hypergeometric functions
hyp1 = mp.hyp2f1(mp.mpf(-1)/4, mp.mpf(1)/4, 1, mp.mpf(1)/2)
hyp2 = mp.hyp2f1(mp.mpf(1)/4, mp.mpf(3)/4, 1, mp.mpf(1)/2)

# Calculate the ratio of gamma functions squared
gamma_ratio_sq = (gamma_14**2) / (gamma_34**2)

# Compute the expression inside the brackets
bracket_term = gamma_ratio_sq * hyp1 - hyp2

# Prefactor: gamma(1/4)^2 / (16 * sqrt(2*pi))
prefactor = gamma_14**2 / (16 * mp.sqrt(2 * mp.pi))

# Final result
result = prefactor * bracket_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))