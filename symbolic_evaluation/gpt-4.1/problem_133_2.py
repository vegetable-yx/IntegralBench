import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
k = 0
# Tolerance for convergence (1e-15 to ensure 10 decimal places accuracy)
tol = mp.mpf('1e-15')
max_iter = 1000  # Maximum iterations to prevent infinite loop

while k < max_iter:
    # Compute power term: 2^(-(2k+1)/2)
    power_term = mp.power(2, - (2*k + 1) / 2)
    
    # Compute numerator gamma functions: Γ(k + 1/2) and Γ(k/2 + 1)
    gamma_num1 = mp.gamma(k + mp.mpf('0.5'))
    gamma_num2 = mp.gamma(k/2 + 1)
    numerator = gamma_num1 * gamma_num2
    
    # Compute denominator gamma functions: Γ(k+1) [k!], Γ(k+2), Γ(3k/2 + 3/2)
    gamma_den1 = mp.gamma(k + 1)   # k! = Γ(k+1)
    gamma_den2 = mp.gamma(k + 2)   # Γ(k+2)
    gamma_den3 = mp.gamma(3*k/2 + mp.mpf('1.5'))
    denominator = gamma_den1 * gamma_den2 * gamma_den3
    
    # Calculate term and add to total
    term = power_term * numerator / denominator
    total += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tol:
        break
    k += 1

# Print the result to exactly 10 decimal places
print(mp.nstr(total, n=10))