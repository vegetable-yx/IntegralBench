import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (since not specified, using a=1.0)
a = mp.mpf(1.0)

# Precompute constant factor: sqrt(pi)/2
factor = mp.sqrt(mp.pi) / 2

# Initialize the series sum
series_sum = mp.mpf(0)

# Tolerance for stopping the series (1e-15)
tol = mp.mpf(1e-15)

# Start with k=0 term
k = 0
# Compute numerator: a^(2k) * Gamma(k+2)
num = a**(2*k) * mp.gamma(k+2)
# Compute denominator: 4^k * (k!)^2 * (2k+3) * Gamma(k+5/2)
denom = (4**k) * (mp.factorial(k)**2) * (2*k + 3) * mp.gamma(k + 2.5)
term = num / denom
series_sum += term

# Initialize k for the loop
k = 1
while True:
    # Compute recurrence factor to update the term
    num_recur = a**2 * (k + 1) * (2*k + 1)
    denom_recur = 4 * (k**2) * (2*k + 3) * (k + 1.5)
    recurrence_factor = num_recur / denom_recur
    
    # Update the current term using recurrence
    term = term * recurrence_factor
    series_sum += term
    
    # Check for convergence
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Multiply by the constant factor to get final result
result = factor * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))