import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values, can be modified)
a = 1.0
b = 1.0

# Convert to mpmath floats for consistent precision
a_val = mp.mpf(a)
b_val = mp.mpf(b)

# Initialize sum and term counter
s = mp.mpf(0)
n = 0
# Tolerance for convergence (1e-15) and maximum terms to prevent infinite loop
tolerance = mp.mpf('1e-15')
max_terms = 1000

while n < max_terms:
    # Compute base: (b^2 * a)^n
    base_power = (b_val**2 * a_val) ** n
    
    # Compute factorial term: (2n)!
    factorial_term = mp.fac(2 * n)
    
    # Compute gamma factors in numerator:
    #   Gamma((2n+5)/4) and Gamma((2n+3)/4)
    gamma_num1 = mp.gamma(mp.mpf(2*n + 5) / 4)
    gamma_num2 = mp.gamma(mp.mpf(2*n + 3) / 4)
    gamma_product = gamma_num1 * gamma_num2
    
    # Compute denominator gamma term: Gamma(n+2)
    gamma_denom = mp.gamma(n + 2)
    
    # Combine components for the term (without leading a)
    term_core = base_power / factorial_term * gamma_product / gamma_denom
    
    # Apply leading factor a to get full term
    term = a_val * term_core
    
    # Add term to the sum
    s += term
    
    # Check for convergence (absolute value of term < tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(s, n=10))