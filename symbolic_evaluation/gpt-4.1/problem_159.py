import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (user can modify these values)
a = mp.mpf(1.0)
b = mp.mpf(1.0)

# Initialize the sum
series_sum = mp.mpf(0)
k = 0
max_iter = 1000
tolerance = mp.mpf('1e-20')

# Sum the series until convergence or max_iter reached
while k < max_iter:
    # Compute base = b^2 * a
    base_val = b**2 * a
    
    # Calculate (base_val)^k
    base_power = base_val ** k
    
    # Compute denominator: (2k)!
    denom_fact = mp.factorial(2 * k)
    
    # Compute numerator gamma functions: Gamma((3+k)/2) and Gamma(1 + k/2)
    gamma_num1 = mp.gamma((3 + k) / 2)
    gamma_num2 = mp.gamma(1 + k / 2)
    
    # Compute denominator gamma function: Gamma(5/2 + k)
    gamma_denom = mp.gamma(5/2 + k)
    
    # Combine gamma functions: numerator product divided by denominator
    gamma_ratio = (gamma_num1 * gamma_num2) / gamma_denom
    
    # Compute current term in the series
    term = base_power / denom_fact * gamma_ratio
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (if term is below tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Multiply the series sum by a^(3/2)
result = a**(mp.mpf(3)/2) * series_sum

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))