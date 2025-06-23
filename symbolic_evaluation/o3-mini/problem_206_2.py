import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Calculate the confluent hypergeometric function _1F_1(1/4; 1/2; -1)
hyp1f1_14 = mp.hyp1f1(mp.mpf(1)/4, mp.mpf(1)/2, -1)

# First term: Gamma(1/4) * _1F_1(1/4; 1/2; -1)
term1 = gamma_14 * hyp1f1_14

# Calculate Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Calculate the confluent hypergeometric function _1F_1(3/4; 3/2; -1)
hyp1f1_34 = mp.hyp1f1(mp.mpf(3)/4, mp.mpf(3)/2, -1)

# Second term: 2 * Gamma(3/4) * _1F_1(3/4; 3/2; -1)
term2 = 2 * gamma_34 * hyp1f1_34

# Combine the two terms
sum_terms = term1 + term2

# Multiply by sqrt(pi)/4
result = (mp.sqrt(mp.pi) / 4) * sum_terms

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))