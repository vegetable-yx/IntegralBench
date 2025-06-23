import mpmath as mp

mp.dps = 15  # Set internal precision

a = mp.mpf('1')  # User can modify a and b values here
b = mp.mpf('1')

sum_part = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Termination criterion for series convergence

while True:
    # Calculate (ab)^(2n)
    ab_pow = (a * b) ** (2 * n)
    
    # Compute factorial terms in numerator
    fact_n_plus2 = mp.factorial(n + 2)
    fact_n = mp.factorial(n)
    
    # Compute denominator components
    two_pow_2n = 2 ** (2 * n)
    fact_2n = mp.factorial(2 * n)
    dfact_2n3 = mp.factorial2(2 * n + 3)  # Double factorial
    
    # Calculate current term
    term = (ab_pow * fact_n_plus2 * fact_n) / (two_pow_2n * fact_2n * dfact_2n3)
    
    sum_part += term
    
    # Check convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by a^3 for final result
result = a ** 3 * sum_part

# Output with 10 decimal precision
print(mp.nstr(result, n=10))