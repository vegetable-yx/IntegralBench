import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: 2^(-1/4)
factor1 = mp.power(2, -0.25)

# Calculate the ratio of Gamma functions: Γ(1/4) / Γ(3/4)
gamma_ratio = mp.gamma(0.25) / mp.gamma(0.75)

# Compute the confluent hypergeometric function: _0F_1(;5/4; -1/4)
hyp0f1_val = mp.hyp0f1(1.25, -0.25)

# Combine all components
result = factor1 * gamma_ratio * hyp0f1_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))