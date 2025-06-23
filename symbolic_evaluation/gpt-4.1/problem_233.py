import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Precompute constant denominator factor: Gamma(3/2)
gamma_3_2 = mp.gamma(mp.mpf('3/2'))

# Initialize sum and start at n=0
s = mp.mpf(0)
n = 0
# Set tolerance for term convergence (sufficient for 10 decimal places)
tolerance = mp.mpf('1e-20')
max_terms = 10000  # Prevent infinite loops

while n < max_terms:
    # Compute Gamma(n + 3/2)
    gamma_n_3_2 = mp.gamma(n + mp.mpf('3/2'))
    # Compute Gamma(1/4 + n/2)
    gamma_1_4_n_2 = mp.gamma(mp.mpf('1/4') + n/2)
    # Compute Gamma(3/4 + n/2)
    gamma_3_4_n_2 = mp.gamma(mp.mpf('3/4') + n/2)
    
    # Numerator: product of three Gamma functions
    numerator = gamma_n_3_2 * gamma_1_4_n_2 * gamma_3_4_n_2
    
    # Denominator: Gamma(3/2) * (n!)^2
    n_factorial = mp.factorial(n)
    denominator = gamma_3_2 * n_factorial**2
    
    # Calculate current term
    term = numerator / denominator
    s += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print final result to exactly 10 decimal places
print(mp.nstr(s, n=10))