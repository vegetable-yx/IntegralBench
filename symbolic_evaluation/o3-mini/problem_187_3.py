import mpmath as mp
mp.dps = 15

from mpmath import mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant term: 11 + sqrt(120)
c = 11 + mp.sqrt(120)

# Compute the argument for Gamma and hypergeometric functions: 1/(11+sqrt(120))
a = 1 / c

# Compute Gamma function in numerator: Gamma(a)
gamma_num = mp.gamma(a)

# Compute the argument for the denominator Gamma: 1/2 + a
b = mp.mpf(0.5) + a

# Compute Gamma function in denominator: Gamma(b)
gamma_den = mp.gamma(b)

# Compute the hypergeometric function: _2F_1(a, 1, b, -1)
hyp2f1 = mp.hyp2f1(a, 1, b, -1)

# Calculate the constant factor: sqrt(pi) / [4 * (11+sqrt(120))]
constant_factor = mp.sqrt(mp.pi) / (4 * c)

# Compute the entire expression: constant_factor * (gamma_num / gamma_den) * hyp2f1
result = constant_factor * (gamma_num / gamma_den) * hyp2f1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))