import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the elliptic integrals: 1/sqrt(2)
k = mp.mpf(1) / mp.sqrt(2)

# Compute the logarithmic term: π * ln((√2 + 1)/2)
log_arg = (mp.sqrt(2) + 1) / 2
term1 = mp.pi * mp.log(log_arg)

# Compute the complete elliptic integrals
E_val = mp.ellipe(k)   # Complete elliptic integral of the second kind
K_val = mp.ellipk(k)   # Complete elliptic integral of the first kind

# Compute the elliptic part: √2 * [2E(1/√2) - K(1/√2)]
term2 = mp.sqrt(2) * (2 * E_val - K_val)

# Sum the two terms to get the result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))