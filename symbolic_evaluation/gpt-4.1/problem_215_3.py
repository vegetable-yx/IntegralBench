import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
n = 0
# Tolerance for stopping the summation (1e-15)
tolerance = mp.mpf('1e-15')
# Maximum terms to prevent infinite loops
max_terms = 1000

while n < max_terms:
    # Compute numerator: (-1)^n * [Gamma(n + 3/4)]^2
    gamma_term = mp.gamma(n + mp.mpf('3/4'))
    numerator = (-1)**n * (gamma_term ** 2)
    
    # Compute denominator: (2n)! * Gamma(2n + 3/2)
    factorial_term = mp.factorial(2 * n)
    gamma_denom = mp.gamma(2 * n + mp.mpf('3/2'))
    denominator = factorial_term * gamma_denom
    
    # Compute current term
    term = numerator / denominator
    total += term
    
    # Check if term magnitude is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print result to exactly 10 decimal places
print(mp.nstr(total, n=10))