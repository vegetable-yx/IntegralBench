import mpmath as mp

# Set internal decimal precision to 15 for accurate 10 decimal place result
mp.dps = 15

# Calculate each component separately with comments

# Compute Γ(3/4) and square it
gamma_val = mp.gamma(mp.mpf(3)/4)
gamma_sq = gamma_val ** 2

# Compute the hypergeometric function _2F_1(-1/4, 1/2; 7/4; 1/2)
hyp2f1_val = mp.hyp2f1(mp.mpf(-1)/4, mp.mpf(1)/2, mp.mpf(7)/4, mp.mpf(1)/2)

# Compute the constant factor √2
sqrt2 = mp.sqrt(2)

# Combine numerator: √2 * [Γ(3/4)]^2 * _2F_1(...)
numerator = sqrt2 * gamma_sq * hyp2f1_val

# Divide by 3 to get final result
result = numerator / 3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))