import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

total = mp.mpf(0)  # Initialize the total sum
k = 0  # Start with k=0

while True:
    # Calculate numerator components: Gamma(k/2 +1) and Gamma((k+3)/2)
    gamma1 = mp.gamma(k/2 + 1)
    gamma2 = mp.gamma((k + 3)/2)
    numerator = gamma1 * gamma2
    
    # Calculate denominator components: 2^(2k+1), k!, (k+1)!, Gamma(k + 5/2)
    exp_term = mp.power(2, 2*k + 1)
    fact_k = mp.factorial(k)
    fact_k1 = mp.factorial(k + 1)
    gamma_denom = mp.gamma(k + mp.mpf('5/2'))
    denominator = exp_term * fact_k * fact_k1 * gamma_denom
    
    term = numerator / denominator  # Compute the current term
    total += term  # Add the term to the total
    
    # Check if the term is smaller than the tolerance (1e-15)
    if mp.fabs(term) < 1e-15:
        break
    
    k += 1  # Move to the next term

# Print the result with exactly 10 decimal places
print(mp.nstr(total, n=10))