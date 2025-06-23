import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (set to 1 as a specific value for computation)
a_val = mp.mpf(1)

# Initialize the sum
sum_val = mp.mpf(0)

# Tolerance for stopping the series
tol = mp.mpf('1e-15')

# Maximum number of terms to prevent infinite loops
max_terms = 1000

# Compute the term for k=0
k0 = 0
# Numerator: a^(2*0) * sqrt(pi) * Gamma(0+2)
numerator0 = a_val**(2*k0) * mp.sqrt(mp.pi) * mp.gamma(k0 + 2)
# Denominator: 4^0 * (0!)^2 * 2 * (2*0+3) * Gamma(0 + 5/2)
denominator0 = (4**k0) * (mp.factorial(k0)**2) * 2 * (2*k0 + 3) * mp.gamma(k0 + 2.5)
term = numerator0 / denominator0
sum_val += term

# If the first term is below tolerance, skip further computation
if mp.fabs(term) < tol:
    pass
else:
    # Start from k=1
    k = 1
    while k <= max_terms:
        # Compute factor for recurrence: t_k = t_{k-1} * factor
        # Factor = [a^2 * (k+1) * (2k+1)] / [2 * k^2 * (2k+3)^2]
        numerator_factor = a_val**2 * (k + 1) * (2*k + 1)
        denominator_factor = 2 * (k**2) * ((2*k + 3)**2)
        factor = numerator_factor / denominator_factor
        
        # Update current term using recurrence
        term = term * factor
        sum_val += term
        
        # Check if term is below tolerance
        if mp.fabs(term) < tol:
            break
        k += 1

# Print the result to 10 decimal places
print(mp.nstr(sum_val, n=10))