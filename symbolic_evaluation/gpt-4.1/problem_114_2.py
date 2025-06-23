import mpmath as mp

# Set internal precision
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)

# Outer constant factor: -sqrt(pi)/2
const = -mp.sqrt(mp.pi) / 2

# Tolerance for series convergence
tol = mp.mpf('1e-15')
max_terms = 10000

# Start the series from n=1 (n=0 term is zero)
for n in range(1, max_terms + 1):
    # (-1)^n / n!
    sign = 1 if n % 2 == 0 else -1
    inv_fact = sign / mp.factorial(n)
    
    # (pi/2) * [(-1)^n / n!]
    term = (mp.pi / 2) * inv_fact
    
    # (1/2)_n: Pochhammer symbol (rising factorial)
    pochhammer = mp.rf(0.5, n)
    
    # Denominator: 1 - 2n
    denom = 1 - 2 * n
    
    # Gamma(n+1/2) / Gamma(n)
    gamma_ratio = mp.gamma(n + 0.5) / mp.gamma(n)
    
    # Digamma difference: psi(n+1/2) - psi(n)
    digamma_diff = mp.digamma(n + 0.5) - mp.digamma(n)
    
    # Multiply all factors
    term *= pochhammer * gamma_ratio * digamma_diff / denom
    
    # Add term to the series sum
    s += term
    
    # Check for convergence
    if mp.fabs(term) < tol:
        break

# Multiply by the outer constant
result = const * s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))