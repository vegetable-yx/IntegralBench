import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Si(1) - Sine Integral of 1
si_1 = mp.si(1)

# Compute sin(1)
sin_1 = mp.sin(1)

# Compute (π/2) * J₀(1) using Bessel function of the first kind
pi_over_2 = mp.pi / 2
j0_1 = mp.besselj(0, 1)
term3 = pi_over_2 * j0_1

# Compute the integral using series expansion to avoid numerical integration
integral = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate numerator and denominator components
    numerator = (-1) ** k
    denominator = (2 * k + 1) * (4 ** k) * (mp.factorial(k) ** 2)
    term = (mp.pi / 2) * numerator / denominator
    
    # Add term to integral sum
    integral += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    k += 1

# Combine all components for final result
result = si_1 - sin_1 + term3 - integral

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))