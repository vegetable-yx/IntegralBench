import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of a (set to 1.0 for this computation)
a_val = mp.mpf(1.0)

# Initialize the series sum and variables
series_sum = mp.mpf(0)  # Holds the sum of the series
n = 0                   # Initialize term index
tolerance = mp.mpf('1e-15')  # Convergence tolerance

# Compute the infinite series until terms become negligible
while True:
    # Calculate (-1)^n
    sign = mp.mpf(1) if n % 2 == 0 else mp.mpf(-1)
    
    # Compute a^(2n+1)
    exponent = 2*n + 1
    a_power = mp.power(a_val, exponent)
    
    # Compute 2^(2n+1)
    two_power = mp.power(2, exponent)
    
    # Compute n! and (n+1)!
    fac_n = mp.factorial(n)
    fac_n1 = mp.factorial(n+1)
    
    # Denominator: 2^(2n+1) * n! * (n+1)! * (2n+1)
    denominator = two_power * fac_n * fac_n1 * (2*n + 1)
    
    # Calculate the current term: (-1)^n * a^(2n+1) / denominator
    term = sign * a_power / denominator
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (term magnitude below tolerance)
    if mp.fabs(term) < tolerance:
        break
    
    # Move to next term
    n += 1

# Multiply by π to get the final result
result = mp.pi * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))