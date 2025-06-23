import mpmath as mp
mp.dps = 15

# Calculate the infinite series component
sum_part = mp.mpf(0)
n = 0
while True:
    # Compute current term: (-1)^n divided by (n!^2 * (2n+1))
    term = ((-1)**n) / ( (mp.factorial(n)**2) * (2*n + 1) )
    sum_part += term
    
    # Check if term is smaller than 1e-15 magnitude for convergence
    if mp.fabs(term) < 1e-15:
        break
    n += 1

# Combine components and multiply by pi
result = mp.pi * (0.5 - sum_part)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))