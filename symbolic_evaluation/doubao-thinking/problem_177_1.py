import mpmath as mp

mp.dps = 15  # Set internal precision

a = mp.mpf(1)  # Define the parameter 'a' (adjust value as needed)

prefactor = mp.pi**(mp.mpf(3)/2) / 4  # Calculate the constant prefactor
result = mp.mpf(0)  # Initialize the result

tolerance = mp.mpf('1e-20')  # Convergence tolerance
max_terms = 100  # Maximum number of terms for each summation

# Outer summation over n
for n in range(max_terms):
    # Calculate components dependent on n index
    sign_n = (-1)**n
    a_power = a**(2*n + 1)
    denominator_n = (2*n + 1) * mp.factorial(n)
    outer_term = sign_n * a_power / denominator_n
    
    # Inner summation over m
    inner_sum = mp.mpf(0)
    for m in range(max_terms):
        # Calculate components dependent on m index
        factorial_2m_sq = (mp.factorial(2*m))**2
        denominator_m = (mp.factorial(m)**3) * (2**(4*m + 2*n)) * mp.gamma(m + n + mp.mpf('5/2'))
        inner_term = factorial_2m_sq / denominator_m
        
        inner_sum += inner_term
        
        # Check inner term convergence
        if mp.fabs(inner_term) < tolerance:
            break
    
    # Add contribution from current n to total result
    n_contribution = outer_term * inner_sum
    result += n_contribution
    
    # Check outer term convergence
    if mp.fabs(n_contribution) < tolerance:
        break

# Apply the prefactor after summation
result *= prefactor

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))