import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Tolerance for convergence check
tol = 1e-15
max_k = 1000  # Maximum number of outer terms

total = mp.mpf(0)
k = 0
while k <= max_k:
    inner_sum = mp.mpf(0)
    # Precompute 2^(4k+2) for current k to avoid repeated calculation
    denom_base = mp.power(2, 4*k + 2)
    
    # Inner sum over n from 0 to k
    for n in range(0, k + 1):
        # Calculate binomial coefficients: binom(2n, n) and binom(2(k-n), k-n)
        binom1 = mp.binomial(2*n, n)
        binom2 = mp.binomial(2*(k - n), k - n)
        
        # Compute denominator components
        denom1 = 2*n + 1
        denom2 = 2*(k - n) + 1
        
        # Combine all denominator terms
        denominator = denom_base * denom1 * denom2
        
        # Add term to inner sum
        inner_sum += binom1 * binom2 / denominator
    
    # Compute outer factor components
    sqrt_pi = mp.sqrt(mp.pi)
    gamma1 = mp.gamma(k + 1.5)  # Gamma(k + 3/2)
    gamma2 = mp.gamma(k + 2)     # Gamma(k+2) = (k+1)!
    
    # Compute outer factor
    numerator = sqrt_pi * gamma1
    denominator_outer = 4 * (k + 1) * gamma2
    outer_factor = numerator / denominator_outer
    
    # Compute complete term for current k
    term_k = inner_sum * outer_factor
    total += term_k
    
    # Check for convergence
    if abs(term_k) < tol:
        break
    
    k += 1

# Print final result with 10 decimal places
print(mp.nstr(total, n=10))