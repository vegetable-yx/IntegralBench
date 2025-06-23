import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize sum and tolerance
s = mp.mpf(0)
tol = mp.mpf('1e-15')
n = 0

# Sum the series until terms are below tolerance
while True:
    # Calculate sign: (-1)^n
    sign = (-1) ** n
    
    # Calculate 2^n
    power2n = mp.power(2, n)
    
    # Calculate Gamma(n+1)
    gamma_n1 = mp.gamma(n + 1)
    
    # Calculate Gamma(n + 1/2)
    gamma_n_half = mp.gamma(n + mp.mpf('0.5'))
    
    # Calculate Gamma(2n+2)
    gamma_2n2 = mp.gamma(2 * n + 2)
    
    # Denominator: (2n+1)! * Gamma(2n+2) = [Gamma(2n+2)]^2 since (2n+1)! = Gamma(2n+2)
    denominator = gamma_2n2 ** 2
    
    # Compute term numerator
    numerator = sign * power2n * gamma_n1 * gamma_n_half
    
    # Compute the term
    term = numerator / denominator
    
    # Add term to the sum
    s += term
    
    # Check if term magnitude is below tolerance
    if mp.fabs(term) < tol:
        break
    
    n += 1

# Print result to 10 decimal places
print(mp.nstr(s, n=10))