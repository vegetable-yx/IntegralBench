import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)
k = 0

while True:
    # Calculate numerator components
    numerator = 4 * mp.sqrt(2) * (k + 1)
    
    # Calculate denominator components
    denominator_part1 = (2*k + 1) * (2*k + 3)
    binomial_coeff = mp.binomial(2*k, k)
    denominator = denominator_part1 * binomial_coeff
    
    # Compute current term
    term = numerator / denominator
    
    # Add term to result
    result += term
    
    # Check if term is smaller than 1e-15 to ensure convergence
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1

print(mp.nstr(result, n=10))