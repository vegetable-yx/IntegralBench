import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constant factor: sqrt(pi)/4
const_factor = mp.sqrt(mp.pi) / 4

# Initialize the sum for the series
series_sum = mp.mpf(0)

# Tolerance for convergence (1e-25) and maximum iterations
tol = mp.mpf('1e-25')
max_iter = 100

# Iterate from n=1 to max_iter
for n in range(1, max_iter + 1):
    # Compute numerator: [(2n)!]^2
    numerator = mp.fac(2 * n) ** 2
    
    # Compute denominator components
    n_cubed = mp.power(n, 3)           # n^3
    n_factorial = mp.fac(n)             # n!
    n_fac_fifth = n_factorial ** 5      # (n!)^5
    pow_64n = mp.power(64, n)           # 64^n
    
    # Combine denominator: n^3 * (n!)^5 * 64^n
    denominator = n_cubed * n_fac_fifth * pow_64n
    
    # Calculate the term for current n
    term = numerator / denominator
    
    # Add term to series sum
    series_sum += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tol:
        break

# Multiply the series sum by the constant factor
result = const_factor * series_sum

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))