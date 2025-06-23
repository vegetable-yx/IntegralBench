import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (arbitrary values, can be adjusted as needed)
a = mp.mpf(1)
b = mp.mpf(1)

# Tolerance for series convergence
tol = mp.mpf('1e-15')
max_iter = 10000  # Prevent infinite loops

# Initialize the series sum (without the a^3 factor)
series_sum = mp.mpf(0)

# Compute the n=0 term explicitly
term = mp.mpf(1)/3  # (n+2)! n! / ((2n)! (2n+3)!) for n=0: (2! * 0!) / (0! * 3!) = 2/6
series_sum += term

# Iterate to compute subsequent terms using recurrence relation
n = 1
while n < max_iter:
    # Update term for current n using recurrence:
    # term(n) = term(n-1) * (a*b)^2 * (n+2)*n / [(2n-1)*(2n)*(2n+2)*(2n+3)]
    denom = (2*n - 1) * (2*n) * (2*n + 2) * (2*n + 3)
    term = term * (a*b)**2 * (n+2) * n / denom
    
    series_sum += term
    
    # Check for convergence (term magnitude below tolerance)
    if abs(term) < tol:
        break
    
    n += 1

# Multiply by a^3 to get final result
result = a**3 * series_sum

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))