import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute the denominator: 32 * sqrt(2 * pi)
denom_part = 32 * mp.sqrt(2 * mp.pi)

# Compute the hypergeometric function 2F1(-1/2, 1/4; 3/4; 1/4)
hyp_val = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(3)/4, mp.mpf(1)/4)

# Combine all parts: (gamma_sq * hyp_val) / denom_part
result = (gamma_sq * hyp_val) / denom_part

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))