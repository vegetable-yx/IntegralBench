import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Precompute sequence A_m to avoid redundant calculations
A_list = []
total = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')

while True:
    # Compute A_k for current k
    m = k
    # Calculate numerator: (2m)!
    num = mp.fac(2 * m)
    # Calculate denominator: (m!)^2 * (2m+1) * 2^(3m+1)
    denom = mp.fac(m) ** 2 * (2 * m + 1) * (2 ** (3 * m + 1))
    A_k = num / denom
    A_list.append(A_k)
    
    # Compute inner sum: convolution of A_list with itself at index k
    inner_sum = mp.mpf(0)
    for n in range(0, k + 1):
        inner_sum += A_list[n] * A_list[k - n]
    
    # Compute outer factor components
    gamma_k2 = mp.gamma(k + 2)      # Γ(k+2)
    gamma_k2p5 = mp.gamma(k + 2.5)  # Γ(k+2.5)
    numerator = mp.sqrt(mp.pi) * gamma_k2
    denominator = 2 * (2 * k + 4) * gamma_k2p5
    outer_factor = numerator / denominator
    
    # Compute term for current k
    term = inner_sum * outer_factor
    total += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    k += 1
    
    # Safeguard against infinite loop
    if k > 1000:
        break

# Print result to 10 decimal places
print(mp.nstr(total, n=10))