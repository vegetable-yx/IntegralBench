import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute the exponential factor e^{-1/4}
exp_factor = mp.exp(-mp.mpf(1)/4)

# Compute each term in the expression separately

# First term: Γ(5/2) * 2^{5/2} * _1F_1(-2, 5/2, 1/4)
gamma1 = mp.gamma(mp.mpf(5)/2)   # Γ(5/2)
pow1 = mp.power(2, mp.mpf(5)/2)  # 2^{5/2}
hyp1 = mp.hyp1f1(-2, mp.mpf(5)/2, mp.mpf(1)/4)  # _1F_1(-2; 5/2; 1/4)
term1 = gamma1 * pow1 * hyp1

# Second term: 20 * Γ(3/2) * 2^{3/2} * _1F_1(-1, 3/2, 1/4)
gamma2 = mp.gamma(mp.mpf(3)/2)   # Γ(3/2)
pow2 = mp.power(2, mp.mpf(3)/2)  # 2^{3/2}
hyp2 = mp.hyp1f1(-1, mp.mpf(3)/2, mp.mpf(1)/4)  # _1F_1(-1; 3/2; 1/4)
term2 = 20 * gamma2 * pow2 * hyp2

# Third term: 60 * Γ(1/2) * 2^{1/2} * _1F_1(0, 1/2, 1/4)
gamma3 = mp.gamma(mp.mpf(1)/2)   # Γ(1/2)
pow3 = mp.power(2, mp.mpf(1)/2)  # 2^{1/2}
hyp3 = mp.hyp1f1(0, mp.mpf(1)/2, mp.mpf(1)/4)  # _1F_1(0; 1/2; 1/4)
term3 = 60 * gamma3 * pow3 * hyp3

# Combine terms: term1 - term2 + term3
bracket = term1 - term2 + term3

# Final result: (e^{-1/4}/2) * bracket
result = (exp_factor / 2) * bracket

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))