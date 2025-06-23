import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)

# Tolerance for stopping the series (1e-15)
tol = mp.mpf('1e-15')

# Maximum number of terms to prevent infinite loops
max_terms = 10000

# Start with k=1
k = 1

while k <= max_terms:
    # Compute arguments for the beta function
    x = mp.mpf('0.25') + k / mp.mpf('2')  # 1/4 + k/2
    y = mp.mpf('0.75') + k / mp.mpf('2')  # 3/4 + k/2
    
    # Calculate the beta function: B(x,y) = gamma(x)*gamma(y)/gamma(x+y)
    beta_val = mp.beta(x, y)
    
    # Compute the current term: beta_val / k^2
    term = beta_val / (k * k)
    
    # Add term to the total sum
    total += term
    
    # If term is smaller than tolerance, break the loop
    if term < tol:
        break
    
    # Increment k for next term
    k += 1

# Print the result to exactly 10 decimal places
print(mp.nstr(total, n=10))