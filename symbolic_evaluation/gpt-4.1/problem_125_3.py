import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Precompute constant factor (π/2)^2
const_factor = (mp.pi / 2) ** 2

total = mp.mpf(0)  # Initialize total sum
n = 0
max_n = 500  # Maximum number of terms in outer sum
tol = mp.mpf('1e-30')  # Tolerance for term convergence

while n < max_n:
    # Compute central binomial coefficient: (2n choose n)
    binom_2n_n = mp.binomial(2*n, n)
    
    # Compute the normalization factor: [ (2n)! / (2^{2n} (n!)^2) ] = binom_2n_n / 4^n
    norm_factor = binom_2n_n / (4**n)
    
    # Square the normalization factor for the outer term
    outer_coeff = norm_factor ** 2
    
    # Initialize inner sum for fixed n
    inner_sum = mp.mpf(0)
    m = 0
    max_m = 1000  # Maximum number of terms in inner sum
    
    while m < max_m:
        # Compute binomial coefficient: binomial(-1/2, m)
        binom_neg_half_m = mp.binomial(-0.5, m)
        
        # Compute the beta function: Γ(n+3)Γ(m+1)/Γ(n+m+4) = B(n+3, m+1)
        beta_val = mp.beta(n+3, m+1)
        
        # Compute the sign term: (-1)^m
        sign = mp.mpf(-1)**m
        
        # Compute the denominator: 2m+1
        denom = 2*m + 1
        
        # Compute the inner term
        term_m = sign * binom_neg_half_m**2 * beta_val / denom
        
        # Add term to inner sum
        inner_sum += term_m
        
        # Break if term is below tolerance
        if mp.fabs(term_m) < tol:
            break
            
        m += 1
    
    # Compute the full term for n: outer_coeff * inner_sum
    term_n = outer_coeff * inner_sum
    total += term_n
    
    # Break if term_n is below tolerance
    if mp.fabs(term_n) < tol:
        break
        
    n += 1

# Multiply by constant factor
result = const_factor * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))