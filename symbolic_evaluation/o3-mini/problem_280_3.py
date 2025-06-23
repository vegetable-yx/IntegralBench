import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (replace with actual values if different)
a = 1.0
b = 1.0

# Compute sqrt(a)
sqrt_a = mp.sqrt(a)

# Compute Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square the Gamma value
gamma_sq = gamma_val ** 2

# Compute numerator: 2 * [Gamma(3/4)]^2
numerator = 2 * gamma_sq

# Compute denominator: sqrt(pi)
denom = mp.sqrt(mp.pi)

# Compute constant factor: 2 * Gamma(3/4)^2 / sqrt(pi)
const_factor = numerator / denom

# Compute argument for hypergeometric function: (b^2 * a^2)/16
z_arg = (b**2 * a**2) / 16

# Compute hypergeometric function {}_0F_1(; 5/4; z_arg)
hyp_val = mp.hyp0f1(mp.mpf(5)/4, z_arg)

# Multiply all components: sqrt(a) * const_factor * hyp_val
result = sqrt_a * const_factor * hyp_val

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))