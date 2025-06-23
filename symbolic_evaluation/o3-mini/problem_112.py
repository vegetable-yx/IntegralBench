import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)

# Convergence tolerance (1e-20) and maximum terms (10000)
tol = mp.mpf('1e-20')
max_terms = 10000

# Compute the series sum
for n in range(1, max_terms + 1):
    n_val = mp.mpf(n)  # Convert n to mpmath float
    # Calculate arguments for gamma functions
    arg1 = n_val/2 + mp.mpf('0.25')  # n/2 + 1/4
    arg2 = n_val/2 - mp.mpf('0.25')  # n/2 - 1/4
    
    # Compute the term using loggamma for numerical stability
    log_term = mp.loggamma(arg1) + mp.loggamma(arg2) - mp.loggamma(n_val)
    term = mp.exp(log_term) / (n_val**2)
    
    total += term
    
    # Break if term is below tolerance after initial terms
    if n > 10 and mp.fabs(term) < tol:
        break

# Apply the 1/2 factor outside the summation
result = total * mp.mpf('0.5')

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))