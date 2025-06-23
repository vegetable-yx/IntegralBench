import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant prefactor: 2^(1/4) / sqrt(pi)
two_14 = mp.power(2, mp.mpf(1)/4)  # 2^{1/4}
prefactor = two_14 / mp.sqrt(mp.pi)

# Initialize the series sum
series_sum = mp.mpf(0)
n = 0
# Set tolerance for convergence (1e-20) and max terms to avoid infinite loop
tolerance = mp.mpf('1e-20')
max_terms = 1000

while n < max_terms:
    # Compute numerator: 2^(n + 1/2)
    num1 = mp.power(2, n + mp.mpf('0.5'))
    
    # Compute denominator: (2n+1)!
    denom1 = mp.factorial(2*n + 1)
    
    # First part: 2^{n+1/2} / (2n+1)!
    part1 = num1 / denom1
    
    # Gamma arguments
    gamma_arg1 = (n + 3) / mp.mpf(4)  # (n+3)/4
    gamma_arg2 = (n + 1) / mp.mpf(4)  # (n+1)/4
    gamma_arg3 = (n + 2) / mp.mpf(2)  # (n+2)/2
    
    # Compute Gamma values
    gamma1 = mp.gamma(gamma_arg1)
    gamma2 = mp.gamma(gamma_arg2)
    gamma3 = mp.gamma(gamma_arg3)
    
    # Second part: [Gamma((n+3)/4) * Gamma((n+1)/4)] / Gamma((n+2)/2)
    part2 = (gamma1 * gamma2) / gamma3
    
    # Term for current n: part1 * part2
    term = part1 * part2
    series_sum += term
    
    # Break if term falls below tolerance
    if mp.fabs(term) < tolerance:
        break
    n += 1

# Multiply by prefactor to get final result
result = prefactor * series_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))