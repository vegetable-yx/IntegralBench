import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma(3/4) and square it
gamma_3_4 = mp.gamma(3/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Compute Gamma(3/2)
gamma_3_2 = mp.gamma(3/2)

# Calculate the ratio: (Gamma(3/4)^2) / Gamma(3/2)
ratio = gamma_3_4_sq / gamma_3_2

# Compute the confluent hypergeometric limit function _0F_1(; 3/2; -1/4)
hyp = mp.hyp0f1(3/2, -1/4)

# Multiply the ratio by the hypergeometric function to get the final result
result = ratio * hyp

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))