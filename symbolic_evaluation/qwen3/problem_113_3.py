import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute components of the coefficient
gamma_val = mp.gamma(mp.mpf('0.25'))  # Gamma(1/4)
sqrt2 = mp.sqrt(2)                    # Square root of 2
pi = mp.pi                            # Pi constant

# Calculate the coefficient (sqrt(2)*pi)/Gamma(1/4)^2
gamma_squared = gamma_val ** 2
coefficient = (sqrt2 * pi) / gamma_squared

# Compute the infinite series sum
sum_part = mp.mpf(0)
n = 1
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate numerator and denominator components
    factorial_2n = mp.factorial(2 * n)
    factorial_n_sq = (mp.factorial(n)) ** 2
    denominator = (8 ** n) * (n ** 2) * factorial_n_sq
    
    # Compute current term and add to sum
    term = factorial_2n / denominator
    sum_part += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    n += 1

# Calculate final result and print
result = coefficient * sum_part
print(mp.nstr(result, n=10))