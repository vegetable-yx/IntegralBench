import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum with the k=0 term
total = mp.mpf(2)  # This is the term for k=0

# Set the current term to the k=0 term
current_term = mp.mpf(2)

# Initialize k for the next term (k=1)
k = 1

# Tolerance for convergence (1e-15)
tolerance = mp.mpf('1e-15')

# Maximum number of terms to prevent infinite loops
max_terms = 1000

# Sum terms from k=1 to infinity until convergence
while k <= max_terms:
    # Compute recurrence factor: 1/(2*k*(2*k+1))
    factor = mp.mpf(1) / (2 * k * (2*k + 1))
    
    # Update current term using recurrence relation
    current_term *= factor
    
    # Add current term to the total sum
    total += current_term
    
    # Check for convergence (absolute value of term < tolerance)
    if mp.fabs(current_term) < tolerance:
        break
    
    k += 1

# Multiply the sum by sqrt(2) to get the final result
result = mp.sqrt(2) * total

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))