import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: 2^{1/4} / sqrt(pi)
const_factor = mp.power(2, mp.mpf('0.25')) / mp.sqrt(mp.pi)

# Initialize the sum
series_sum = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-20')  # Convergence tolerance
max_iter = 1000  # Maximum iterations to prevent infinite loops

# Sum the series until convergence
while k < max_iter:
    # Compute exponent for 2: (2k+1)/2
    exponent = mp.mpf(2*k + 1) / 2
    power_term = mp.power(2, exponent)
    
    # Gamma function arguments
    gamma_arg1 = mp.mpf(k + 3) / 4  # (k+3)/4
    gamma_arg2 = mp.mpf(k + 1) / 4  # (k+1)/4
    gamma_arg3 = mp.mpf(k + 2) / 2  # (k+2)/2
    
    # Compute gamma values
    gamma1 = mp.gamma(gamma_arg1)
    gamma2 = mp.gamma(gamma_arg2)
    gamma3 = mp.gamma(gamma_arg3)
    
    # Factorial in denominator: (2k+1)!
    factorial_term = mp.factorial(2*k + 1)
    
    # Compute the term: [2^{(2k+1)/2} * Γ((k+3)/4) * Γ((k+1)/4)] / [(2k+1)! * Γ((k+2)/2)]
    numerator = power_term * gamma1 * gamma2
    denominator = factorial_term * gamma3
    term = numerator / denominator
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (term magnitude below tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Multiply by constant factor to get final result
result = const_factor * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))