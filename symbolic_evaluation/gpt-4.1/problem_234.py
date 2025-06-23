import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Initialize the sum
total = mp.mpf(0)

# Tolerance for truncating the series (small enough for 10 decimal places)
tol = 1e-15

# Start from n=1
n = 1

# Sum the series until terms become negligible
while True:
    # Calculate the arguments for the beta function
    a = (n + 1) / 2
    b = (n + 2) / 2
    
    # Compute the beta function: B(a,b) = gamma(a)*gamma(b)/gamma(a+b)
    beta_val = mp.beta(a, b)
    
    # Compute the term: n * B(a, b)
    term = n * beta_val
    
    # Add term to the total
    total += term
    
    # Check if the term is below tolerance (since terms are positive, absolute value is the term itself)
    if term < tol:
        break
    
    # Next term
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))