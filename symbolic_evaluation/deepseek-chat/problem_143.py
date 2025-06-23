import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (assumed to be 1.0 for numerical evaluation)
a = mp.mpf(1.0)

# Precompute z = a^2 / 4
z = a**2 / 4

# Constant factor: sqrt(pi)/8
const_factor = mp.sqrt(mp.pi) / 8

# Initialize the series sum
series_sum = mp.mpf(0)

# Tolerance for convergence (1e-20) and maximum terms (1000)
tolerance = mp.mpf('1e-20')
max_terms = 1000
k = 0

# Sum the series until convergence or max_terms reached
while k < max_terms:
    # Compute z^k
    z_power = z**k
    
    # Compute Gamma(k + 1.5)
    gamma_val = mp.gamma(k + 1.5)
    
    # Compute factorial(k) and factorial(k+1)
    fact_k = mp.factorial(k)
    fact_k1 = mp.factorial(k + 1)
    
    # Denominator: (k+1)^3 * factorial(k) * factorial(k+1)
    denom = (k + 1)**3 * fact_k * fact_k1
    
    # Compute the current term
    term = z_power * gamma_val / denom
    series_sum += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

# Multiply by the constant factor to get the final result
result = const_factor * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))