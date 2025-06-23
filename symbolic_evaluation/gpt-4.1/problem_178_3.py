import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the total sum to zero
total = mp.mpf(0)

# Tolerance for term magnitude to break loops
tol = mp.mpf('1e-30')

# Maximum values for k and l indices
kmax = 100
lmax = 100

# Iterate over k from 0 to kmax
for k in range(0, kmax + 1):
    # Initialize sum for current row (fixed k)
    row_sum = mp.mpf(0)
    # Flag to check if breaking at l=0
    broke_at_l0 = False
    
    # Iterate over l from 0 to lmax
    for l in range(0, lmax + 1):
        # Determine the sign (-1)^(k+l)
        sign = mp.mpf(1) if (k + l) % 2 == 0 else mp.mpf(-1)
        
        # Compute k! and l!
        fac_k = mp.factorial(k)
        fac_l = mp.factorial(l)
        
        # Compute Gamma(k + 3.5) and Gamma(l + 1.5)
        gamma_k = mp.gamma(k + mp.mpf('3.5'))
        gamma_l = mp.gamma(l + mp.mpf('1.5'))
        
        # Compute denominator: k! * l! * Gamma(k+3.5) * Gamma(l+1.5)
        denom = fac_k * fac_l * gamma_k * gamma_l
        
        # Compute arguments for the beta function: 2k+1.5 and 2l+1.5
        a = 2 * k + mp.mpf('1.5')
        b = 2 * l + mp.mpf('1.5')
        
        # Compute beta function value: B(a, b) = Gamma(a) * Gamma(b) / Gamma(a+b)
        beta_val = mp.beta(a, b)
        
        # Compute the current term
        term = sign * beta_val / denom
        
        # Add the term to the row sum
        row_sum += term
        
        # Check if the absolute value of the term is below tolerance
        if mp.fabs(term) < tol:
            # If breaking at l=0, set flag to break outer loop later
            if l == 0:
                broke_at_l0 = True
            # Break the inner loop
            break
    
    # Add the row sum to the total
    total += row_sum
    
    # If broke at l=0, break the outer loop (remaining rows negligible)
    if broke_at_l0:
        break

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))