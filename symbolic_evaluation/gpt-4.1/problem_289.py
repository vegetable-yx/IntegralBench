import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (chosen as 1.0 for numerical evaluation)
a = mp.mpf(1.0)

# Initialize the total sum
total = mp.mpf(0)

# Tolerances for breaking loops
outer_tol = mp.mpf('1e-20')
inner_tol = mp.mpf('1e-20')

# Maximum iterations for m and n loops
max_m = 200
max_n = 10000

# Precompute constant factors
a_half = a / 2
pi = mp.pi

# Outer loop over m
for m in range(0, max_m):
    # Sign factor (-1)^m
    sign = mp.mpf(-1)**m
    # (a/2)^(2m+1)
    power_factor = a_half**(2*m + 1)
    
    # Denominator: Gamma(m+3/2) * Gamma(m+1)
    gamma_m_plus_3_2 = mp.gamma(m + 1.5)  # m+3/2 = m+1.5
    gamma_m_plus_1 = mp.gamma(m + 1)
    denom = gamma_m_plus_3_2 * gamma_m_plus_1
    
    # Initialize inner sum over n
    inner_sum = mp.mpf(0)
    
    # Inner loop over n
    for n in range(0, max_n):
        # Central binomial coefficient: binomial(2n, n)
        binom_val = mp.binomial(2*n, n)
        # Squared binomial coefficient
        binom_sq = binom_val**2
        # 16^n
        power16 = mp.mpf(16)**n
        # Term: [binom(2n,n)^2] / 16^n
        binom_term = binom_sq / power16
        
        # Beta function: Beta(m+5/2, n+1) = Beta(m+2.5, n+1)
        beta_val = mp.beta(m + 2.5, n + 1)
        
        # Term for fixed n: binom_term * beta_val
        term_n = binom_term * beta_val
        inner_sum += term_n
        
        # Break inner loop if term_n is below tolerance (since terms are positive)
        if term_n < inner_tol:
            break
    
    # Outer term for fixed m: sign * power_factor * inner_sum / denom
    outer_term = sign * power_factor * inner_sum / denom
    total += outer_term
    
    # Break outer loop if |outer_term| is below tolerance
    if mp.fabs(outer_term) < outer_tol:
        break

# Multiply by pi/4 to get the final result
result = total * pi / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))