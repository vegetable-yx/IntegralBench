import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)
# Tolerance for convergence
tolerance = mp.mpf('1e-20')
# Maximum number of terms to prevent infinite loops
max_terms = 100

n = 0
while n <= max_terms:
    # Calculate the central binomial coefficient: C(2n, n)
    binom_val = mp.binomial(2*n, n)
    
    # Compute the squared binomial coefficient divided by 64^n
    binom_sq = binom_val**2
    power_64n = mp.power(64, n)
    coef1 = binom_sq / power_64n
    
    # Divide by (n+1) to get the coefficient part
    coef = coef1 / (n + 1)
    
    # Parameters for the hypergeometric function _3F_2
    a_params = [-mp.mpf('0.5'), mp.mpf('0.5'), 1]
    b_params = [1, n + 2]
    
    # Evaluate the hypergeometric function at z=1
    hyp_val = mp.hyper(a_params, b_params, 1)
    
    # Compute the term: coefficient * hypergeometric value
    term = coef * hyp_val
    total += term
    
    # Check for convergence: break if term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by the constant factor π²/4
pi_sq = mp.pi**2
result = (pi_sq / 4) * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))