import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (arbitrarily set to 1.0 for computation)
a = 1.0

# Precompute the constant factor: sqrt(pi)/4
const_factor = mp.sqrt(mp.pi) / 4

# Initialize the series sum
series_sum = mp.mpf(0)

# Set convergence tolerance and maximum terms to avoid infinite loops
tolerance = 1e-15
max_terms = 1000
k = 0

while k < max_terms:
    # Compute numerator: Gamma(k + 3/2)
    num = mp.gamma(k + 1.5)
    
    # Compute denominator components
    # (k!)^2 = [Gamma(k+1)]^2
    gamma_k1 = mp.gamma(k + 1)
    gamma_k1_sq = gamma_k1 ** 2
    
    # (k+1) term
    k_plus1 = k + 1
    
    # Gamma(k+2) = Gamma(k+1+1) = (k+1)*Gamma(k+1)
    gamma_k2 = k_plus1 * gamma_k1
    
    # Full denominator: (k!)^2 * (k+1) * Gamma(k+2)
    denom = gamma_k1_sq * k_plus1 * gamma_k2
    
    # Compute the term: [Gamma(k+3/2)] / [denominator] * (a^2/4)^k
    term = num / denom * (a**2 / 4) ** k
    
    # Break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    # Add term to series sum
    series_sum += term
    k += 1

# Multiply the series sum by the constant factor
result = const_factor * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))