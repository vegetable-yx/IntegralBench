import mpmath as mp

mp.dps = 15  # Set internal precision

total = mp.mpf(0)
n = 1
tolerance = mp.mpf(1e-15)

while True:
    sign = (-1) ** (n + 1)  # Alternating sign term
    denominator = n * (3 ** n)  # Compute denominator n*3^n
    gamma_ratio = mp.gamma(n/2) / mp.gamma(n/2 + 0.5)  # Gamma function terms ratio
    term = sign * gamma_ratio / denominator  # Combine components for current term
    total += term  # Accumulate the sum
    
    if mp.fabs(term) < tolerance:  # Check for convergence
        break
    n += 1

result = total * mp.sqrt(mp.pi)  # Multiply by sqrt(pi) as per formula
print(mp.nstr(result, n=10))