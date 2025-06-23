import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Example values for parameters a and b (user can modify these)
a = mp.mpf(1.0)
b = mp.mpf(1.0)

# Common argument for both hypergeometric functions: b^4 * a / 64
z_arg = (b**4 * a) / 64

# Calculate the first hypergeometric term:
# T1 = (sqrt(pi) * a^(3/2) / 4 * _1F_2(1/2; 3/4, 5/4; z_arg)
coeff1 = (mp.sqrt(mp.pi) * a**(mp.mpf(3)/2)) / 4
hyper_term1 = mp.hyper([mp.mpf(0.5)], [mp.mpf(0.75), mp.mpf(1.25)], z_arg)
term1 = coeff1 * hyper_term1

# Calculate the second hypergeometric term:
# T2 = (b^2 * a^2) / 8 * _1F_2(1; 5/4, 3/2; z_arg)
coeff2 = (b**2 * a**2) / 8
hyper_term2 = mp.hyper([mp.mpf(1)], [mp.mpf(1.25), mp.mpf(1.5)], z_arg)
term2 = coeff2 * hyper_term2

# Combine both terms for final result
result = term1 + term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))