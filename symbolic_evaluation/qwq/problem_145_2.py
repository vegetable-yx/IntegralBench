import mpmath as mp

mp.dps = 15  # Set internal precision

result = mp.mpf(0)  # Initialize result
k = 0               # Starting index
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate numerator components: 4^k and k!
    pow4 = mp.power(4, k)
    fact_k = mp.factorial(k)
    numerator = pow4 * fact_k
    
    # Calculate denominator components: (2k+1)^2, (2k)!, (k+1)!
    denom_term1 = mp.power(2*k + 1, 2)
    denom_term2 = mp.factorial(2*k)
    denom_term3 = mp.factorial(k + 1)
    denominator = denom_term1 * denom_term2 * denom_term3
    
    # Compute current term and add to result
    term = numerator / denominator
    result += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < tolerance:
        break
    k += 1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))