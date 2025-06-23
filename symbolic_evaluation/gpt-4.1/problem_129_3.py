import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
k = 0
# Tolerance for convergence (1e-15 ensures 10 decimal accuracy)
tol = mp.mpf('1e-15')
max_iter = 10000  # Safeguard against non-convergence

# Main summation loop
while k < max_iter:
    # Calculate numerator: Gamma((k+3)/2)
    num_arg = mp.mpf(k + 3) / 2
    numerator = mp.gamma(num_arg)
    
    # Calculate denominator components
    factorial_k = mp.factorial(k)      # k!
    pow_2k = mp.power(2, k)            # 2^k
    denom_arg = mp.mpf(3*k + 5) / 2    # Argument for Gamma in denominator
    gamma_denom = mp.gamma(denom_arg)  # Gamma((3k+5)/2)
    
    denominator = factorial_k * pow_2k * gamma_denom
    term = numerator / denominator
    
    total += term
    
    # Check if term is below tolerance
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Multiply by constant factor 2√2
constant = 2 * mp.sqrt(2)
result = constant * total

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))