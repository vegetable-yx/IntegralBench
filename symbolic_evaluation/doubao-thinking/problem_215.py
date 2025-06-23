import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance to stop the summation

while True:
    # Calculate the current term's Gamma(n + 3/4) and square it
    gamma_n_plus_3_4 = mp.gamma(n + mp.mpf('3/4'))
    gamma_squared = gamma_n_plus_3_4 ** 2
    
    # Calculate denominator components: (2n)! and Gamma(2n + 3/2)
    factorial_2n = mp.factorial(2 * n)
    gamma_2n_plus_3_2 = mp.gamma(2 * n + mp.mpf('3/2'))
    denominator = factorial_2n * gamma_2n_plus_3_2
    
    # Compute the current term with alternating factor (-1)^n
    term = ((-1) ** n) * gamma_squared / denominator
    sum_result += term
    
    # Check if the term is smaller than the tolerance to break the loop
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print the result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))