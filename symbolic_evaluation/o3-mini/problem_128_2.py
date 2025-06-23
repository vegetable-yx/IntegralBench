import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each component of the constant factor
# 2^(1/4)
base = 2
exponent = mp.mpf(1)/4
two_power = base ** exponent

# e^(1/2)
e_power = mp.exp(mp.mpf(1)/2)

# Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Denominator: 2 * sqrt(pi)
denom = 2 * mp.sqrt(mp.pi)

# Compute constant factor: (2^(1/4) * e^(1/2) * Gamma(3/4)) / (2*sqrt(pi))
constant = (two_power * e_power * gamma_val) / denom

# Evaluate Whittaker W function at k=-1/8, mu=1/4, z=1
k_val = mp.mpf(-1)/8
mu_val = mp.mpf(1)/4
z_val = 1
whitw_val = mp.whitw(k_val, mu_val, z_val)

# Multiply constant by Whittaker W value
result = constant * whitw_val

# Print final result to exactly 10 decimal places
print(mp.nstr(result, n=10))