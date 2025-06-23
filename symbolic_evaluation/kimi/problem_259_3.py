import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)
n = 0
# We'll break when terms become negligible (below 1e-15 in absolute value)
max_iter = 1000  # Safeguard to prevent infinite loops

for n in range(max_iter):
    # Compute numerator: (-1)^n * gamma(n+2)
    numerator = (-1)**n * mp.gamma(n + 2)
    
    # Compute denominator: (2n+1)! * (n+2) * gamma(n+2.5)
    factorial_term = mp.fac(2*n + 1)   # (2n+1)!
    gamma_term = mp.gamma(n + 2.5)     # gamma(n+2.5)
    denominator = factorial_term * (n + 2) * gamma_term
    
    # Compute the term for this n
    term = numerator / denominator
    
    # Add term to the sum
    s += term
    
    # Check for convergence: if |term| < 1e-15, break
    if mp.fabs(term) < 1e-15:
        break

# Multiply by the constant factor: sqrt(pi)/2
result = (mp.sqrt(mp.pi) / 2) * s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))