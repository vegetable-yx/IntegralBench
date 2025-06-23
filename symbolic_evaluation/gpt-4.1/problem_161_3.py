import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_terms = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-20')  # Tolerance for convergence check

while True:
    # Calculate numerator and denominator components
    numerator = mp.power(2, n)
    denominator = mp.factorial(2 * n)
    
    # Compute Gamma function terms
    gamma_num1 = mp.gamma((5 + 2 * n) / 4)
    gamma_num2 = mp.gamma((3 + 2 * n) / 4)
    gamma_den = mp.gamma(2 + n)
    
    # Calculate the current term
    term = (numerator / denominator) * (gamma_num1 * gamma_num2) / gamma_den
    sum_terms += term
    
    # Check if the term is smaller than the convergence tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply the sum by 2 as per the original expression
result = 2 * sum_terms

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))