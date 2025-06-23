import mpmath as mp

# Set internal precision
mp.dps = 15

# Precompute constant factor: 2 * sqrt(2)
const = 2 * mp.sqrt(2)

# Initialize the sum and tolerance
total = mp.mpf(0)
tolerance = mp.mpf('1e-20')
max_iter = 1000
k = 0

while k <= max_iter:
    # Compute 2^{-k}
    exp_term = mp.power(2, -k)
    
    # Compute factorial term: 1/(k!)^2
    fact_term = 1 / (mp.factorial(k) ** 2)
    
    # Gamma function arguments
    arg1 = mp.mpf(3)/2 + mp.mpf(k)/2  # 3/2 + k/2
    arg2 = 1 + mp.mpf(k)/2             # 1 + k/2
    arg3 = mp.mpf(5)/2 + k             # 5/2 + k
    
    # Compute Gamma values
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    gamma3 = mp.gamma(arg3)
    
    # Combine gamma terms: [Gamma(3/2 + k/2) * Gamma(1 + k/2)] / Gamma(5/2 + k)
    gamma_ratio = (gamma1 * gamma2) / gamma3
    
    # Compute the term for current k
    term = const * exp_term * fact_term * gamma_ratio
    total += term
    
    # Check convergence condition
    if mp.fabs(term) < tolerance:
        break
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))