import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
series_sum = mp.mpf(0)
n = 1
max_iter = 10000  # Maximum number of iterations to prevent infinite loops
tolerance = mp.mpf('1e-15')  # Tolerance for stopping the summation

while n <= max_iter:
    # Convert n to mpmath float for high precision
    n_val = mp.mpf(n)
    
    # Compute arguments for gamma functions: a = n/2 + 1/4, b = n/2 - 1/4
    a = n_val / 2 + mp.mpf('0.25')
    b = n_val / 2 - mp.mpf('0.25')
    
    # Compute the term: Γ(a) * Γ(b) / (n^2 * Γ(n))
    # Using beta function identity: Γ(a)Γ(b)/Γ(a+b) = B(a,b) and a+b = n
    term = mp.beta(a, b) / (n_val**2)
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (since all terms are positive)
    if term < tolerance:
        break
    
    n += 1

# Multiply by 1/2 as per the formula
result = series_sum * mp.mpf('0.5')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))