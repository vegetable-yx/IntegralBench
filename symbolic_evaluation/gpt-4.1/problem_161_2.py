import mpmath as mp

mp.dps = 15

sum_part = mp.mpf(0)
n = 0
term = mp.mpf(1)  # Initialize term to enter loop

while mp.fabs(term) > 1e-15:
    # Calculate components of the term
    power_term = mp.power(2, n)
    factorial_term = mp.factorial(2 * n)
    
    gamma_num1 = mp.gamma((n + 3)/2)
    gamma_num2 = mp.gamma((3 + 2*n)/4)
    gamma_denom = mp.gamma((4*n + 9)/4)
    
    # Combine components for current term
    term = (power_term / factorial_term) * (gamma_num1 * gamma_num2 / gamma_denom)
    sum_part += term
    
    n += 1

# Multiply by 2 from the outer summation coefficient
result = 2 * sum_part

print(mp.nstr(result, n=10))