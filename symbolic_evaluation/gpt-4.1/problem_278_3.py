import mpmath as mp

mp.dps = 15

sum_total = mp.mpf(0)
k = 0
epsilon = mp.mpf('1e-15')

while True:
    # Calculate 4^k
    pow_4k = 4 ** k
    # Calculate factorial of 2k
    factorial_2k = mp.fac(2 * k)
    # Calculate Gamma(k + 3/2)
    gamma_k_3_2 = mp.gamma(k + mp.mpf('3/2'))
    # Calculate Gamma(k + 1/2)
    gamma_k_1_2 = mp.gamma(k + mp.mpf('1/2'))
    # Calculate Gamma(2k + 2)
    gamma_2k_2 = mp.gamma(2 * k + 2)
    # Compute the current term
    term = (pow_4k / factorial_2k) * (gamma_k_3_2 * gamma_k_1_2) / gamma_2k_2
    sum_total += term
    # Check if the term is smaller than epsilon
    if mp.fabs(term) < epsilon:
        break
    k += 1

# Multiply the sum by 2 as per the formula
result = 2 * sum_total

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))