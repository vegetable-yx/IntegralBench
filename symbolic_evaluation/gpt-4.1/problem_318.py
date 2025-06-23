import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Define the value of parameter 'a' (user can change this as needed)
a = 1.0

# Precompute constant factor: sqrt(pi)/4
const_factor = mp.sqrt(mp.pi) / 4

# Initialize sum and variables for series computation
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for term convergence
max_iter = 1000  # Maximum iterations to prevent infinite loops

# Compute series until convergence or max iterations
while n < max_iter:
    # Calculate sign: (-1)^n
    sign = (-1)**n
    
    # Compute a^(2n+1)
    power_term = a**(2*n + 1)
    
    # Calculate Gamma(n+1)
    gamma_n1 = mp.gamma(n + 1)
    
    # Compute denominator components
    n_plus_1 = n + 1
    factorial_2n1 = mp.factorial(2*n + 1)  # (2n+1)!
    gamma_n32 = mp.gamma(n + 1.5)  # Gamma(n + 3/2)
    
    # Full denominator: (n+1) * (2n+1)! * Gamma(n+3/2)
    denominator = n_plus_1 * factorial_2n1 * gamma_n32
    
    # Compute current term: [(-1)^n * a^(2n+1) * Gamma(n+1)] / denominator
    term = (sign * power_term * gamma_n1) / denominator
    
    # Add term to series sum
    series_sum += term
    
    # Check if term magnitude is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply series sum by constant factor
result = const_factor * series_sum

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))