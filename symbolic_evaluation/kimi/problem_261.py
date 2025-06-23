import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize the sum
m = 0  # Start with m=0

while True:
    # Calculate numerator: (-1)^m * 2^(2m) * (m!)^2
    numerator = (-1)**m * (2**(2*m)) * (mp.fac(m)**2)
    
    # Calculate denominator: m! * Gamma(m+1) * (2m+1) * (2m+1)!
    # Since Gamma(m+1) = m!, denominator simplifies to (m!)^2 * (2m+1) * (2m+1)!
    denominator = (mp.fac(m)**2) * (2*m + 1) * mp.fac(2*m + 1)
    
    term = numerator / denominator  # Compute current term
    
    sum_result += term  # Add term to the sum
    
    # Check if term is smaller than 1e-15 to ensure precision beyond 10 decimal places
    if mp.fabs(term) < 1e-15:
        break
    
    m += 1  # Increment m for next iteration

# Print the result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))