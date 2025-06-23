import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
n = 0
epsilon = mp.mpf(1e-20)  # Termination threshold for term magnitude

while True:
    # Calculate components for current term
    power_term = 4 ** (n + 2)
    numerator_factorials = mp.factorial(n + 2) * mp.factorial(n + 1)
    denominator_factorial = mp.factorial(2 * n + 4)
    denominator_components = 2 * (2 * n + 3) * (mp.factorial(n) ** 2)
    
    # Compute complete term
    term = (power_term * numerator_factorials) / (denominator_components * denominator_factorial)
    
    sum_result += term
    
    # Check convergence
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

print(mp.nstr(sum_result, n=10))