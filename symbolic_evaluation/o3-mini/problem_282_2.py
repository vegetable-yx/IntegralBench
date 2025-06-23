import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (example values - user should modify these as needed)
a = 1.0
b = 1.0

# Convert parameters to mpmath floats for precise computation
a_mp = mp.mpf(a)
b_mp = mp.mpf(b)

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square of Gamma(1/4)
gamma_sq = gamma_14 ** 2

# Compute denominator: sqrt(pi) * a^{1/2}
sqrt_pi = mp.sqrt(mp.pi)
sqrt_a = mp.sqrt(a_mp)
denom = sqrt_pi * sqrt_a

# Compute argument for hypergeometric function: (a^2 * b^2)/16
arg = (a_mp**2 * b_mp**2) / 16

# Evaluate hypergeometric function {}_1F_2(1/4; 1/2, 3/4; arg)
hyp = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(3)/4], arg)

# Combine components to compute final result
result = gamma_sq / denom * hyp

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))