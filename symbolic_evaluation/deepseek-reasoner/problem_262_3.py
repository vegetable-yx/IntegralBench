import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
m = 0
epsilon = mp.mpf('1e-20')  # Convergence threshold

while True:
    # Calculate numerator components
    sign = (-1) ** m
    factorial_2m_plus_2 = mp.factorial(2 * m + 2)
    
    # Calculate denominator components
    power_4m = 4 ** m
    factorial_m = mp.factorial(m)
    factorial_m_plus_1 = mp.factorial(m + 1)
    denominator = power_4m * factorial_m * (factorial_m_plus_1 ** 3)
    
    # Compute current term
    term = sign * factorial_2m_plus_2 / denominator
    sum_result += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    m += 1

# Multiply by π/16 and print result
result = (mp.pi / 16) * sum_result
print(mp.nstr(result, n=10))