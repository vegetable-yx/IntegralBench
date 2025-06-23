import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize result as a mpmath floating-point number

# Sum the series expansion terms until convergence
for k in range(0, 50):
    a = mp.mpf(k) + 1.5  # Beta function parameter a = k + 1.5
    b = mp.mpf(0.5)      # Beta function parameter b = 0.5
    beta_term = mp.beta(a, b)  # Compute Beta(a, b)
    factorial_term = mp.factorial(2 * k)  # Compute (2k)!
    term = beta_term / factorial_term  # Calculate current term
    result += term  # Accumulate the term into the result
    
    # Check for convergence (term magnitude below 1e-15)
    if mp.fabs(term) < mp.mpf('1e-15'):
        break

print(mp.nstr(result, n=10))  # Print result with 10 decimal places