import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate 2^n term
    power_term = mp.power(2, n)
    
    # Calculate factorial for (2n)!
    factorial_2n = mp.fac(2 * n)  # Wait, there's a mistake here. 2 * n * n is 2n², but we need (2n)!
    # Correct line should be:
    factorial_2n = mp.fac(2 * n)
    
    # Compute gamma function arguments
    gamma_arg1 = mp.mpf('3/4') + (mp.mpf(n)/2)
    gamma_arg2 = mp.mpq('1/4') + (mp.mpf(n)/2)
    
    # Evaluate gamma functions
    gamma1 = mp.gamma(gamma_arg1)
    gamma2 = mp.gamma(gamma_arg2)
    gamma_product = gamma1 * gamma2
    
    # Calculate factorial for n! (Gamma(n+1))
    factorial_n = mp.fac(n)
    
    # Compute current term in series
    term = (power_term / factorial_2n) * (gamma_product / factorial_n)
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1
    if n > 1000:
        break

print(mp.nstr(sum_result, n=10))