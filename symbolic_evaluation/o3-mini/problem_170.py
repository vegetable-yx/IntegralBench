import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute the hypergeometric function _2F_1(-1/2, 1/2; 1; 1/16)
hyp1 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/2, 1, mp.mpf(1)/16)

# Compute the hypergeometric function _2F_1(1/2, 1/2; 2; 1/16)
hyp2 = mp.hyp2f1(mp.mpf(1)/2, mp.mpf(1)/2, 2, mp.mpf(1)/16)

# Compute the first term: [Gamma(1/4)]^2 * hyp1
term1 = gamma_1_4**2 * hyp1

# Compute the second term: [Gamma(3/4)]^2 * hyp2
term2 = gamma_3_4**2 * hyp2

# Compute the difference: term1 - term2
diff = term1 - term2

# Multiply by 1/64
result = diff / 64

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))