import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (using example values a=1, b=1; can be adjusted)
a_val = mp.mpf(1)
b_val = mp.mpf(1)

# Precompute constant factor: a^(3/2)
factor = a_val**(mp.mpf(3)/2)

# Initialize series sum and variables
series_sum = mp.mpf(0)
k = 0
tol = mp.mpf(1e-15)  # Tolerance for convergence
max_terms = 1000     # Maximum number of terms to prevent infinite loops

while k < max_terms:
    # Compute numerator: (2 * a * b^2)^k
    num = (2 * a_val * b_val**2)**k
    
    # Compute denominator: factorial of 2k
    denom = mp.fac(2*k)
    
    # Arguments for beta function: x = (k+3)/2, y = (k+2)/2
    x_arg = (k + 3) / mp.mpf(2)
    y_arg = (k + 2) / mp.mpf(2)
    
    # Evaluate beta function
    beta_val = mp.beta(x_arg, y_arg)
    
    # Compute current series term
    term = num * beta_val / denom
    series_sum += term
    
    # Check for convergence
    if abs(term) < tol:
        break
    k += 1

# Multiply by the constant factor
result = factor * series_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))