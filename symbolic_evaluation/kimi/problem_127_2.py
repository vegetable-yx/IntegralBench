import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

result = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-25')  # Tolerance for convergence checking

while True:
    # Calculate numerator: Gamma((k+2)/2) * Gamma((k+1)/2)
    gamma1 = mp.gamma((k + 2)/2)
    gamma2 = mp.gamma((k + 1)/2)
    numerator = gamma1 * gamma2

    # Calculate denominator components
    gamma_denom = mp.gamma((2*k + 3)/2)
    pow_term = 2**(k + 0.5)
    fact_k = mp.factorial(k)
    fact_k1 = mp.factorial(k + 1)

    denominator = gamma_denom * pow_term * fact_k * fact_k1

    # Compute current term in the series
    term = numerator / denominator

    # Add term to the result
    result += term

    # Check for convergence
    if mp.fabs(term) < tolerance:
        break

    k += 1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))