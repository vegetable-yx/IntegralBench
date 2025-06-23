import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate Gamma(1/4) and square it
gamma_val = mp.gamma(mp.mpf(1)/4)
gamma_sq = gamma_val ** 2

# Calculate the denominator: 16 * sqrt(2 * pi)
denom = 16 * mp.sqrt(2 * mp.pi)

# Calculate the hypergeometric function: _2F_1(-1/2, 1/4; 3/4; 1/2)
hyp_val = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/4, mp.mpf(3)/4, mp.mpf(1)/2)

# Combine the parts: (Gamma(1/4)^2 / denominator) * hypergeometric value
result = (gamma_sq / denom) * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))