import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Initialize the sum
result = mp.mpf(0)

# Tolerance for convergence (1e-20 is safe for 10 decimal places)
tol = mp.mpf('1e-20')

# Initialize n for the series
n = 0

while True:
    # Compute the numerator: [gamma((3+4n)/4)]^2
    gamma_arg1 = (3 + 4*n) / 4  # = 0.75 + n
    gamma_val = mp.gamma(gamma_arg1)
    numerator = gamma_val**2
    
    # Compute the denominator: gamma((3+4n)/2) * (2n)!
    gamma_arg2 = (3 + 4*n) / 2  # = 1.5 + 2n
    denominator = mp.gamma(gamma_arg2) * mp.factorial(2*n)
    
    # Compute the term: (-1)^n * numerator / denominator
    term = (-1)**n * numerator / denominator
    
    # Add term to the result
    result += term
    
    # Break if the term is below tolerance
    if mp.fabs(term) < tol:
        break
    
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))