import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)
# Tolerance for convergence (1e-15)
tol = mp.mpf('1e-15')
# Maximum number of terms to prevent infinite loops
max_terms = 1000
# Start with k=0
k = 0

while k < max_terms:
    # Calculate numerator: Γ(k/2 + 1) * Γ(k/2 + 1/2)
    num1 = mp.gamma(k/2 + 1)
    num2 = mp.gamma(k/2 + 0.5)
    numerator = num1 * num2
    
    # Calculate denominator: k! * Γ(k+2) * Γ(k+3/2) * 2^(k+1/2)
    denom1 = mp.factorial(k)         # k!
    denom2 = mp.gamma(k + 2)         # Γ(k+2)
    denom3 = mp.gamma(k + 1.5)       # Γ(k+3/2)
    denom4 = mp.power(2, k + 0.5)    # 2^(k+1/2)
    denominator = denom1 * denom2 * denom3 * denom4
    
    # Compute the current term
    term = numerator / denominator
    s += term
    
    # Check for convergence
    if mp.fabs(term) < tol:
        break
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(s, n=10))