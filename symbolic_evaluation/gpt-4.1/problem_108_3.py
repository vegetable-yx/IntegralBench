import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: 4 * sqrt(2) is not directly in the constant? 
# But note: our derivation had constant = sqrt(2) * pi, and then we had a factor from the series?
# Actually, we derived: I = sqrt(2) * pi * (series)
# However, let me recheck the derivation:

# We had:
#   I = 4 * sqrt(2) * integral(...) 
#   and we expanded the elliptic integral E(k) = (pi/2) * hyp2f1(-0.5, 0.5, 1, k^2) with k^2 = 0.25 * sin(2θ)
#   then I = 4 * sqrt(2) * (pi/2) * integral( ... hyp2f1 ... ) 
#        = 2 * sqrt(2) * pi * integral( ... hyp2f1 ... )
#   and then we expanded the hyp2f1 in series and integrated term by term, leading to:
#        I = sqrt(2) * pi * sum_{n=0}^{∞} [ ... ]

# So the constant is sqrt(2)*pi, as we have.

const = mp.sqrt(2) * mp.pi

# Initialize the total sum for the series
total = mp.mpf(0)
n = 0
max_terms = 1000
tolerance = mp.mpf('1e-20')

# Sum the series until convergence or maximum terms
while n < max_terms:
    # Compute the Pochhammer symbols (rising factorials) for a=-0.5 and b=0.5
    a_n = mp.rf(-0.5, n)
    b_n = mp.rf(0.5, n)
    
    # Denominator: (n!)^2 (since (1)_n = n! and then divided by n! in the hypergeometric series)
    denom = mp.factorial(n) ** 2
    
    # Coefficient part: [a_n * b_n / denom] * (0.5)^n
    term_coeff = a_n * b_n / denom
    term_coeff *= (mp.mpf(0.5)) ** n
    
    # Arguments for the beta function: x = (n+3)/2, y = (n+2)/2
    x = (n + 3) / mp.mpf(2)
    y = (n + 2) / mp.mpf(2)
    beta_val = mp.beta(x, y)
    
    # Current term in the series
    term = term_coeff * beta_val
    total += term
    
    # Check for convergence: if term is below tolerance, break
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by the constant factor
result = const * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))