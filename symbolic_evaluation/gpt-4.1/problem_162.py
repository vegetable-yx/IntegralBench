import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (arbitrary values since not specified)
a = mp.mpf('1.0')
b = mp.mpf('1.0')

# Initialize the sum
sum_val = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-30')
max_iter = 1000  # Safeguard to prevent infinite loops

while n < max_iter:
    # Calculate base: (b^2 * a)
    base_val = b**2 * a
    
    # Compute the numerator: (b^2 * a)^n
    base_power = base_val**n
    
    # Compute denominator: factorial of 2n
    factorial_denom = mp.fac(2*n)
    
    # Compute arguments for the beta function
    arg1 = mp.mpf('0.75') + n/2  # 3/4 + n/2
    arg2 = mp.mpf('0.25') + n/2  # 1/4 + n/2
    
    # Evaluate beta function: B(3/4 + n/2, 1/4 + n/2)
    beta_val = mp.beta(arg1, arg2)
    
    # Compute current term: [ (b^2 a)^n / (2n)! ] * beta(3/4+n/2, 1/4+n/2)
    term = base_power / factorial_denom * beta_val
    
    # Add term to the sum
    sum_val += term
    
    # Check for convergence (if term magnitude below tolerance)
    if mp.fabs(term) < tolerance:
        break
        
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(sum_val, n=10))