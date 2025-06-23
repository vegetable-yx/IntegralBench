import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (user can modify these values)
a = 1.0  # Example value for a, can be changed
b = 1.0  # Example value for b, can be changed

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square Gamma(1/4)
gamma_sq = gamma_14 ** 2

# Compute denominator: sqrt(pi) * sqrt(a)
denom = mp.sqrt(mp.pi) * mp.sqrt(a)

# Compute argument for hypergeometric function: (b^2 * a^2) / 16
z = (b**2 * a**2) / 16

# Compute hypergeometric function _0F_1(; 1/4; z)
hyper = mp.hyp0f1(mp.mpf(1)/4, z)

# Combine components: numerator = gamma_sq * hyper, then divide by denom
result = gamma_sq * hyper / denom

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))