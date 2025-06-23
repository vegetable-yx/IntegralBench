import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of a (set to 1.0 as default)
a = mp.mpf(1.0)

# Initialize the sum and variables for the series
result = mp.mpf(0)
m = 0
tolerance = mp.mpf('1e-25')  # Convergence tolerance
max_iter = 1000  # Maximum number of iterations to prevent infinite loops

# Sum the series until convergence
while m < max_iter:
    # Compute numerator: a^(2m+1)
    numerator = a**(2*m + 1)
    
    # Compute denominator components:
    denom_power = 2**(2*m + 1)          # 2^(2m+1)
    denom_gamma = mp.gamma(m + 1.5)      # Gamma(m + 3/2)
    denom_factorial = mp.factorial(m)    # m!
    denom_offset = m + 0.5               # (m + 1/2)
    
    # Combine denominator components
    denominator = denom_power * denom_gamma * denom_factorial * denom_offset
    
    # Compute the hypergeometric function {}_3F_2(-1/2, 1/2, 1; 1, m+3/2; 1)
    hyper_val = mp.hyper3f2([-0.5, 0.5, 1.0], [1.0, m + 1.5], 1.0)
    
    # Calculate the current term
    term = numerator / denominator * hyper_val
    
    # Add term to the result
    result += term
    
    # Check for convergence (if term is negligible)
    if mp.fabs(term) < tolerance:
        break
    
    m += 1

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))