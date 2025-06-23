import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (example values: a=1.0, b=1.0)
a_val = mp.mpf(1.0)
b_val = mp.mpf(1.0)

# Initialize the sum and set tolerance for convergence
total = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

# Compute the infinite series
while True:
    # Compute (a*b)^(2n)
    ab_power = (a_val * b_val) ** (2 * n)
    
    # Compute Gamma(n+1) and Gamma(n + 1/2)
    gamma_n1 = mp.gamma(n + 1)
    gamma_n_half = mp.gamma(n + 0.5)
    
    # Numerator: (a*b)^(2n) * Gamma(n+1) * Gamma(n+1/2)
    numerator = ab_power * gamma_n1 * gamma_n_half
    
    # Denominator: (2n)! * Gamma(2n+2)
    fac_2n = mp.fac(2 * n)           # (2n)!
    gamma_2n2 = mp.gamma(2 * n + 2)   # Gamma(2n+2) = (2n+1)!
    denominator = fac_2n * gamma_2n2
    
    # Current term in the series
    term = numerator / denominator
    
    # Add term to total
    total += term
    
    # Check for convergence (absolute value to handle complex, but parameters are real)
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by a^{1/2}
result = mp.sqrt(a_val) * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))