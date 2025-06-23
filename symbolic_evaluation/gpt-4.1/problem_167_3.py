import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: 2 * sqrt(pi)
const = 2 * mp.sqrt(mp.pi)

# Initialize the series sum
series_sum = mp.mpf(0)
n = 0
# Tolerance for term magnitude to break the loop (1e-15 ensures 10 decimal accuracy)
tol = mp.mpf('1e-15')

while True:
    # Compute exponent: 2^{-(2n+1)}
    exponent = mp.power(2, -(2*n + 1))
    
    # Denominator: 2n + 1
    denom = 2*n + 1
    
    # Gamma ratio: Γ(n + 3/2) / Γ(n + 2)
    gamma_num = mp.gamma(n + mp.mpf('1.5'))  # Γ(n + 3/2)
    gamma_den = mp.gamma(n + 2)             # Γ(n + 2)
    gamma_ratio = gamma_num / gamma_den
    
    # Argument for elliptic integral: m = (2n+2)/(2n+3) = k^2
    m_val = mp.mpf(2*n + 2) / mp.mpf(2*n + 3)
    
    # Compute complete elliptic integral of the first kind: K(m)
    K_val = mp.ellipk(m_val)
    
    # Compute current term in the series
    term = exponent / denom * gamma_ratio * K_val
    series_sum += term
    
    # Break loop if term magnitude is below tolerance
    if mp.fabs(term) < tol:
        break
    
    n += 1

# Multiply the series sum by the constant factor
result = const * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))