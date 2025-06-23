import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum to zero
result = mp.mpf(0)

# Tolerance for stopping the summation (1e-15)
tol = mp.mpf('1e-15')

# Maximum terms to prevent infinite loops
max_terms = 10000

# Start summation from k=0
k = 0
while k < max_terms:
    # Compute gamma(1 + k/2)
    gamma_val = mp.gamma(1 + k/2)
    
    # Square the gamma value
    gamma_sq = gamma_val**2
    
    # Compute denominator components
    fact_k = mp.factorial(k)
    fact_k1 = mp.factorial(k+1)
    fact_k1_sq = fact_k1**2
    
    # Compute the entire denominator: k! * [(k+1)!]^2
    denominator = fact_k * fact_k1_sq
    
    # Compute numerator: 2^{-k} * [gamma(1 + k/2)]^2
    numerator = mp.power(2, -k) * gamma_sq
    
    # Calculate the term for current k
    term = numerator / denominator
    
    # Add term to the result
    result += term
    
    # Check if term is below tolerance to stop summation
    if term < tol:
        break
    
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))