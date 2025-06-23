import mpmath as mp
mp.dps = 15

result = mp.mpf(0)
n = 0

while True:
    # Compute numerator components: Gamma(n/2 + 1) and Gamma((n + 3)/2)
    gamma_n_half = mp.gamma(n/2 + 1)
    gamma_n3_half = mp.gamma((n + 3)/2)
    numerator = gamma_n_half * gamma_n3_half
    
    # Compute denominator components: 2^(2n+1), n!, (n+1)!, Gamma((2n+5)/2)
    power_term = mp.power(2, 2*n + 1)
    factorial_n = mp.factorial(n)
    factorial_n1 = mp.factorial(n + 1)
    gamma_2n5_half = mp.gamma((2*n + 5)/2)
    denominator = power_term * factorial_n * factorial_n1 * gamma_2n5_half
    
    # Calculate the current term and add to result
    term = numerator / denominator
    result += term
    
    # Break loop if term is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

print(mp.nstr(result, n=10))