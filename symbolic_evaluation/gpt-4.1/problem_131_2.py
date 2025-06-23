import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)

# We'll iterate k from 0 until terms become negligible
k = 0
while True:
    # Compute factorial k! and square it for denominator
    k_fac_sq = mp.factorial(k)**2
    
    # Compute the power term: 2^(-k/2)
    power_term = mp.power(2, -k/2)
    
    # Compute argument for Gamma in numerator: (k + 3/2)/2 = k/2 + 3/4
    gamma_arg = k/2 + 0.75  # 3/4 = 0.75
    
    # Compute Gamma(gamma_arg) and square it for numerator
    gamma_num = mp.gamma(gamma_arg)**2
    
    # Compute Gamma in denominator: Gamma(k + 3/2)
    gamma_den = mp.gamma(k + 1.5)  # 3/2 = 1.5
    
    # Compute the term without the outer factor of 2
    term = power_term / k_fac_sq * gamma_num / gamma_den
    
    # Break if term is too small (below 1e-30) to affect 10 decimal places
    if abs(term) < 1e-30:
        break
    
    # Add term to the sum
    s += term
    
    # Increment k for next iteration
    k += 1

# Multiply the entire sum by 2 as per the formula
result = 2 * s

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))