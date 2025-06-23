import mpmath as mp
mp.dps = 15

sum_terms = mp.mpf(0)
k = 0

while True:
    # Calculate 2^k term
    two_power = mp.power(2, k)
    
    # Compute Gamma((k+1)/2)
    gamma_num1 = mp.gamma((k + 1) / 2)
    
    # Compute Gamma(k/2 + 1)
    gamma_num2 = mp.gamma(k / 2 + 1)
    
    # Compute numerator components
    numerator = two_power * gamma_num1 * gamma_num2
    
    # Compute denominator factorial (2k)!
    factorial_2k = mp.fac(2 * k)
    
    # Compute Gamma((3k + 3)/2)
    gamma_den = mp.gamma((3 * k + 3) / 2)
    
    # Compute full denominator
    denominator = factorial_2k * gamma_den
    
    # Calculate current term in series
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_terms += term
    
    # Break loop if term is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

# Multiply sum by 2*sqrt(2) for final result
result = 2 * mp.sqrt(2) * sum_terms

# Print result with 10 decimal places
print(mp.nstr(result, n=10))