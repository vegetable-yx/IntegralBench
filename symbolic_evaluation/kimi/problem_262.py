import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)  # Initialize result as an mpmath floating-point number
m = 0

while True:
    # Calculate factorial of m
    factorial_m = mp.factorial(m)
    
    # Compute denominator part (m! * Γ(m+1)) which is (m!)^2
    denominator_part1 = factorial_m * mp.gamma(m + 1)
    
    # First component of the term: (-1)^m / (m!^2)
    term1 = ((-1) ** m) / denominator_part1
    
    # Second component: 1/(2m+2)
    term2 = 1 / (2 * (m + 1))
    
    # Compute Γ((2m+3)/2) and denominator 2*Γ(m+2)
    gamma_arg = (2 * m + 3) / 2
    gamma_val = mp.gamma(gamma_arg)
    denominator_part2 = 2 * mp.factorial(m + 1)
    
    # Third component: sqrt(pi)*Γ((2m+3)/2)/(2*Γ(m+2))
    term3 = (mp.sqrt(mp.pi) * gamma_val) / denominator_part2
    
    # Multiply all components to get the current term
    term = term1 * term2 * term3
    
    # Add term to the result
    result += term
    
    # Break loop if term is smaller than 1e-15 (sufficient for 10 decimal precision)
    if mp.fabs(term) < 1e-15:
        break
    
    m += 1  # Increment m for next iteration

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))