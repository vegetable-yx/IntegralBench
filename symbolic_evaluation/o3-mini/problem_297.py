import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi^(3/2)
pi_power = mp.power(mp.pi, mp.mpf('1.5'))

# Compute Gamma(5/4)
gamma_54 = mp.gamma(mp.mpf('5/4'))

# Numerator: pi^(3/2) * Gamma(5/4)
numerator = pi_power * gamma_54

# Compute Gamma(7/4)
gamma_74 = mp.gamma(mp.mpf('7/4'))

# Denominator: 48 * Gamma(7/4)
denominator = 48 * gamma_74

# Fraction: numerator / denominator
fraction = numerator / denominator

# Parameters for the hypergeometric function {}_3F_2
a1 = mp.mpf('0.5')   # 1/2
a2 = mp.mpf('1')     # 1
a3 = mp.mpf('5/4')   # 5/4
b1 = mp.mpf('3/2')   # 3/2
b2 = mp.mpf('7/4')   # 7/4

# Evaluate the hypergeometric function {}_3F_2(1/2,1,5/4; 3/2,7/4; 1)
hyp_val = mp.hyper([a1, a2, a3], [b1, b2], 1)

# Final result: fraction * hypergeometric value
result = fraction * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))