import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
k = 0
eps = mp.mpf(1e-15)  # Convergence threshold

while True:
    # Calculate numerator components
    gamma_k_half = mp.gamma(k/2 + 1)
    gamma_k3_half = mp.gamma((k + 3)/2)
    numerator = gamma_k_half * gamma_k3_half

    # Calculate denominator components
    power_term = 2 ** (2*k + 1)
    fact_k = mp.factorial(k)
    fact_kp1 = mp.factorial(k + 1)
    gamma_denom = mp.gamma((2*k + 5)/2)
    denominator = power_term * fact_k * fact_kp1 * gamma_denom

    term = numerator / denominator
    sum_result += term

    # Check for convergence
    if mp.fabs(term) < eps:
        break

    k += 1

print(mp.nstr(sum_result, n=10))