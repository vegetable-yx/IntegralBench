import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constant factor: 2^(-1/4)
a = mp.power(2, mp.mpf('-1/4'))

# Compute sqrt(pi)
b = mp.sqrt(mp.pi)

# Compute ratio of Gamma functions: Γ(1/8) / Γ(5/8)
gamma_num = mp.gamma(mp.mpf('1/8'))
gamma_den = mp.gamma(mp.mpf('5/8'))
c = gamma_num / gamma_den

# Compute digamma terms
psi_half = mp.digamma(mp.mpf('1/2'))
psi_one_eighth = mp.digamma(mp.mpf('1/8'))
psi_five_eighths = mp.digamma(mp.mpf('5/8'))
psi_one = mp.digamma(mp.mpf('1'))

# Compute the expression inside the brackets
term1 = psi_half - psi_one_eighth
term2 = psi_five_eighths - psi_one
d = term1 - mp.mpf('0.5') * term2

# Combine all parts to get final result
result = a * b * c * d

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))