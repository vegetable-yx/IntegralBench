import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum and the tolerance for convergence
total = mp.mpf(0)
term = mp.mpf(1)  # Initialize term to enter the loop
n = 0
tolerance = mp.mpf('1e-20')  # Tolerance for breaking the loop

# Sum the series until terms become negligible
while True:
    # Calculate numerator components
    gamma1 = mp.gamma(n/2 + 1)
    gamma2 = mp.gamma(n/2 + 0.5)
    numerator = gamma1 * gamma2
    
    # Calculate denominator components
    factorial_n = mp.factorial(n)
    two_power_n = mp.power(2, n)
    gamma_denom = mp.gamma(n + 1.5)
    gamma_denom_sq = mp.power(gamma_denom, 2)
    denominator = factorial_n * two_power_n * gamma_denom_sq
    
    # Compute the current term
    term = numerator / denominator
    
    # Break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    # Add term to total and increment n
    total += term
    n += 1

# Print the result with 10 decimal places
print(mp.nstr(total, n=10))