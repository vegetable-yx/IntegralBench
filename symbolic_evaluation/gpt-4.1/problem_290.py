import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (arbitrarily set to 1 for computation)
a = mp.mpf(1)

# Precompute constant factor: pi/2
factor = mp.pi / 2

# Initialize the sum and variables
total = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')

# Precompute base for the a factor: a^2 / 4
base = (a * a) / 4
# Initial a_factor for k=0: a/2
a_factor_current = a / 2

# Sum the series until terms are negligible
while True:
    # Compute numerator: [Gamma(k + 5/2)]^2
    gamma_num = mp.gamma(k + mp.mpf('2.5'))
    num = gamma_num ** 2
    
    # Compute denominator components
    gamma_denom1 = mp.gamma(k + 3)  # Gamma(k+3)
    gamma_denom2 = mp.gamma(k + mp.mpf('1.5'))  # Gamma(k + 3/2)
    gamma_denom3 = mp.gamma(k + 1)  # Gamma(k+1)
    
    # Combine denominator: [Gamma(k+3)]^2 * Gamma(k+3/2) * Gamma(k+1)
    denom = gamma_denom1 ** 2 * gamma_denom2 * gamma_denom3
    
    # Compute the gamma ratio term
    term_gamma = num / denom
    
    # Multiply by the current a factor (which includes (a/2) * (a^2/4)^k)
    term = term_gamma * a_factor_current
    total += term
    
    # Check if the term is below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    # Update a factor for next iteration: multiply by base (a^2/4)
    a_factor_current *= base
    k += 1

# Multiply the total sum by the constant factor pi/2
result = factor * total

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))