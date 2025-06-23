import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

sum_part = mp.mpf(0)
n = 0
epsilon = mp.mpf(1e-15)  # Convergence threshold

while True:
    # Calculate factorial and denominator components
    factorial_term = mp.factorial(n)
    power_term = 4**n
    denominator = (factorial_term ** 2) * power_term * (2*n + 1)
    
    # Calculate current term with alternating sign
    term = (-1) ** n / denominator
    
    sum_part += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Multiply by π/2 for final result
result = sum_part * (mp.pi / 2)

print(mp.nstr(result, n=10))