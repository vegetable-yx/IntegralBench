import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values)
a = mp.mpf('0.5')
b = mp.mpf('0.5')

# Precompute square root of a
sqrt_a = mp.sqrt(a)

# Compute base for the power term: (b * sqrt(a))^2 = a * b^2
base = a * b**2

# Initialize series sum and k counter
series_sum = mp.mpf(0)
k = 0

# Set tolerance for convergence (1e-15) and maximum terms (1000)
tolerance = mp.mpf('1e-15')
max_terms = 1000

# Loop to compute the infinite series
while k < max_terms:
    # Compute arguments for gamma functions
    arg1 = (k + 1) / mp.mpf(2)       # (k+1)/2
    arg2 = k / mp.mpf(2) + 1          # k/2 + 1
    arg3 = k + mp.mpf('1.5')          # k + 3/2
    
    # Compute gamma function values
    gamma1 = mp.gamma(arg1)           # Γ((k+1)/2)
    gamma2 = mp.gamma(arg2)           # Γ(k/2 + 1)
    gamma3 = mp.gamma(arg3)           # Γ(k + 3/2)
    
    # Compute factorial of 2k
    fact_2k = mp.fac(2*k)
    
    # Compute base^k
    base_power = base**k
    
    # Calculate term value
    term = base_power * gamma1 * gamma2 / (fact_2k * gamma3)
    
    # Add term to series sum
    series_sum += term
    
    # Check for convergence (absolute value of term < tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Multiply by sqrt_a for final result
result = sqrt_a * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))