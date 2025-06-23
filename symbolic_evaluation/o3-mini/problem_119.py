import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf('0.25'))

# Compute A = [Gamma(1/4)]^2
A = gamma_quarter ** 2

# Compute sqrt(2*pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Denominator for the outer fraction: 16 * sqrt(2*pi)
denom_outer = 16 * sqrt_2pi

# Denominator for the inner term: 8 * sqrt(2*pi)
denom_inner = 8 * sqrt_2pi

# Compute the hypergeometric function _2F_1(-1/2, 1/4; 3/4; 1/2)
hyp = mp.hyp2f1(mp.mpf('-0.5'), mp.mpf('0.25'), mp.mpf('0.75'), mp.mpf('0.5'))

# Compute the inner expression: (A / (8*sqrt(2pi))) - hyp
inner_expr = A / denom_inner - hyp

# Compute the entire expression: [A/(16*sqrt(2pi))] * inner_expr
result = (A / denom_outer) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))