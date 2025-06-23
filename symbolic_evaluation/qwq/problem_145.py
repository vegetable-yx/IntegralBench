import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum to zero
total = mp.mpf(0)

# Tolerance for breaking the loop (1e-25 is safe for 10 decimal places)
tolerance = mp.mpf('1e-25')

# Initialize k for the series index
k = 0
# Maximum terms to prevent infinite loops (series converges quickly)
max_terms = 1000

while k < max_terms:
    # Compute numerator: 4^k
    num = mp.power(4, k)
    
    # Compute denominator components
    denom1 = k + 1           # (k+1) term
    denom2 = (2*k + 1) ** 2  # (2k+1)^2 term
    denom3 = mp.factorial(2*k) # (2k)! term
    
    # Convert integer parts to mpf and compute full denominator
    full_denom = mp.mpf(denom1) * mp.mpf(denom2) * denom3
    
    # Calculate the current term
    term = num / full_denom
    
    # Break if term is below tolerance
    if term < tolerance:
        break
    
    # Add term to total
    total += term
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))