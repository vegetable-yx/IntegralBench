import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Square Gamma(1/4)
gamma_14_sq = gamma_14**2

# Compute denominator: 8 * sqrt(2 * pi)
denom = 8 * mp.sqrt(2 * mp.pi)

# Compute digamma function values
digamma_14 = mp.psi(mp.mpf(1)/4)  # ψ(1/4)
digamma_34 = mp.psi(mp.mpf(3)/4)  # ψ(3/4)

# Compute ln(2)
ln2 = mp.log(2)

# Combine the inner expression: ψ(3/4) - ψ(1/4) + 3*ln(2)
inner_expr = digamma_34 - digamma_14 + 3 * ln2

# Combine all components: [Gamma(1/4)^2 / (8*sqrt(2*pi))] * inner_expr
result = (gamma_14_sq / denom) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))