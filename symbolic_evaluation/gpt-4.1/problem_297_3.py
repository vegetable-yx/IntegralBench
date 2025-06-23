import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Tolerance for stopping the summation
tolerance = mp.mpf('1e-30')
# Maximum terms to prevent infinite loops
max_terms = 100

# Initialize the total sum
total = mp.mpf(0)

# Outer loop over m
for m in range(0, max_terms):
    inner_sum = mp.mpf(0)  # Sum over n for fixed m
    # Inner loop over n
    for n in range(0, max_terms):
        # Compute P_m = [ (-1/2)_m * (1/2)_m ] / (m!)^2
        P_m = mp.poch(-0.5, m) * mp.poch(0.5, m) / (mp.factorial(m)**2)
        
        # Compute P_n = [ (-1/2)_n * (1/2)_n ] / (n!)^2
        P_n = mp.poch(-0.5, n) * mp.poch(0.5, n) / (mp.factorial(n)**2)
        
        # Compute F = (m+2)! * n! / (m+n+3)!
        F = mp.factorial(m+2) * mp.factorial(n) / mp.factorial(m+n+3)
        
        # Compute the term: (π²/4) * P_m * P_n * F
        term = (mp.pi**2 / 4) * P_m * P_n * F
        
        inner_sum += term
        
        # Check if the absolute value of the term is below tolerance
        if abs(term) < tolerance:
            break
    
    total += inner_sum
    
    # Check if the entire inner sum for this m is below tolerance
    if abs(inner_sum) < tolerance:
        break

# Print the result with exactly 10 decimal places
print(mp.nstr(total, n=10))