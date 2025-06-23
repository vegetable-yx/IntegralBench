import mpmath as mp

# Set internal decimal places of precision to 15
mp.dps = 15

# Calculate gamma values
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Γ(3/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Γ(1/4)

# Compute the ratio Γ(3/4) / Γ(1/4)
gamma_ratio = gamma_3_4 / gamma_1_4

# Take the natural logarithm of the ratio
log_ratio = mp.log(gamma_ratio)

# Multiply the logarithm of the ratio by 2
two_log_ratio = 2 * log_ratio

# Compute ln(2)
log2 = mp.log(2)

# Sum: 2 * log_ratio + log2
sum_logs = two_log_ratio + log2

# Multiply by -π/4
result = - (mp.pi / 4) * sum_logs

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))