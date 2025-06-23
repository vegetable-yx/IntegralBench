import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate the constant coefficient (3√π)/2
const_coeff = 3 * mp.sqrt(mp.pi) / 2

# Compute complete elliptic integral of the first kind
k_value = mp.ellipk(1 / mp.sqrt(2))

# Initialize series sum and variables
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

# Calculate the infinite series
while True:
    # Compute numerator components
    numerator = (-9) ** n
    
    # Compute denominator components
    factorial_term = mp.fac(2 * n + 1)
    denominator = factorial_term * (2 * n + 1)
    
    # Compute gamma function ratio
    gamma_ratio = mp.gamma(n + mp.mpf('1.5')) / mp.gamma(n + 2)
    
    # Calculate current term
    term = (numerator / denominator) * gamma_ratio
    series_sum += term
    
    # Break condition when term is negligible
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Combine all components for final result
result = const_coeff * k_value * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))