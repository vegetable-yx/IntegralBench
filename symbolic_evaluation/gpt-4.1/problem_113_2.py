import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)

# Tolerance for breaking the loop (1e-15)
tolerance = mp.mpf('1e-15')

# Iterate over k from 1 to a sufficiently large number
k = 1
max_terms = 1000  # Safe upper bound to prevent infinite loops

while k <= max_terms:
    # Convert k to mpmath float for precise arithmetic
    k_mp = mp.mpf(k)
    
    # Calculate arguments for gamma functions
    arg1 = mp.mpf(3)/4 + k_mp/2  # \frac{3}{4} + \frac{k}{2}
    arg2 = mp.mpf(1)/4 + k_mp/2  # \frac{1}{4} + \frac{k}{2}
    
    # Compute numerator: Γ(3/4 + k/2) * Γ(1/4 + k/2)
    gamma1 = mp.gamma(arg1)
    gamma2 = mp.gamma(arg2)
    numerator = gamma1 * gamma2
    
    # Compute denominator: k^2 * Γ(1 + k) = k^2 * k!
    denom1 = k_mp**2
    denom2 = mp.gamma(1 + k_mp)  # Gamma(k+1) = k!
    denominator = denom1 * denom2
    
    # Compute current term
    term = numerator / denominator
    total += term
    
    # Break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))