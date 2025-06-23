import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant values to avoid repeated calculations
half = mp.mpf('0.5')
one_eighth = mp.mpf('0.125')
thirteen_eighth = mp.mpf('1.625')
gamma_half = mp.gamma(half)  # Γ(1/2)
digamma_half = mp.digamma(half)  # ψ(1/2)

# Initialize the sum
total = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')
max_terms = 10000  # Safety limit to prevent infinite loops

while True:
    # Compute binomial coefficient: binom(1/2, k)
    binom_term = mp.binomial(half, k)
    
    # Arguments for gamma and digamma functions
    arg1 = one_eighth + k * half  # 0.125 + k/2
    arg2 = thirteen_eighth + k * half  # 1.625 + k/2
    
    # Compute gamma terms ratio: Γ(1/2) * Γ(0.125 + k/2) / Γ(1.625 + k/2)
    gamma_ratio = gamma_half * mp.gamma(arg1) / mp.gamma(arg2)
    
    # Compute digamma terms: ψ(0.125 + k/2) and ψ(1.625 + k/2)
    digamma_term1 = mp.digamma(arg1)
    digamma_term2 = mp.digamma(arg2)
    
    # Combine digamma terms: ψ(1/2) - (1/2)ψ(0.125 + k/2) + (1/2)ψ(1.625 + k/2)
    digamma_combo = digamma_half - half * digamma_term1 + half * digamma_term2
    
    # Compute the entire term for current k
    term = binom_term * gamma_ratio * digamma_combo
    total += term
    
    # Break if term is below tolerance or max terms reached
    if mp.fabs(term) < tolerance or k >= max_terms:
        break
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))