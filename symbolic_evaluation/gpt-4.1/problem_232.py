import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute Gamma(5/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Compute Gamma(2) - which is exactly 1
gamma_2 = mp.gamma(2)

# Compute the hypergeometric function 2F1(3/4, 5/4; 2; 1)
hyper = mp.hyp2f1(mp.mpf(3)/4, mp.mpf(5)/4, 2, 1)

# Combine the results: [Gamma(3/4)*Gamma(5/4)/Gamma(2)] * 2F1(...)
result = (gamma_3_4 * gamma_5_4) / gamma_2 * hyper

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))