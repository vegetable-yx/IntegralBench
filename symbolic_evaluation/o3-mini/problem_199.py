import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate gamma values
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Γ(1/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Γ(3/4)

# Compute the powers of 2
pow2_1_4 = mp.power(2, mp.mpf(1)/4)  # 2^(1/4)
pow2_3_4 = mp.power(2, mp.mpf(3)/4)  # 2^(3/4)

# Evaluate the hypergeometric terms
hyp1 = mp.hyp0f1(mp.mpf(5)/4, mp.mpf(-1)/8)  # _0F_1(;5/4;-1/8)
hyp2 = mp.hyp0f1(mp.mpf(3)/4, mp.mpf(-1)/8)  # _0F_1(;3/4;-1/8)

# Construct the two main terms
term1 = (gamma_1_4 / pow2_1_4) * hyp1
term2 = (gamma_3_4 / pow2_3_4) * hyp2

# Combine terms to get final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))