import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Square the gamma(3/4) value
gamma_34_sq = gamma_34 ** 2

# Calculate gamma(3/2)
gamma_32 = mp.gamma(mp.mpf(3)/2)

# Compute the hypergeometric function 0F1(; 3/2; -1/4)
hyp0f1_term = mp.hyp0f1(mp.mpf(3)/2, -mp.mpf(1)/4)

# Combine the components: [gamma(3/4)^2 / gamma(3/2)] * hyp0f1(;3/2;-1/4)
result = (gamma_34_sq / gamma_32) * hyp0f1_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))