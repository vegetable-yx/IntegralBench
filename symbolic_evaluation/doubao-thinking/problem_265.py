import mpmath as mp

mp.dps = 15

result = mp.mpf(0)
k = 0

while True:
    # Calculate factorial of k
    factorial_k = mp.factorial(k)
    # Calculate gamma(k + 5/2)
    gamma_term = mp.gamma(k + mp.mpf('5/2'))
    # Compute (-1)^k term
    sign = (-1) ** k
    # Numerator: (-1)^k * sqrt(pi)
    numerator = sign * mp.sqrt(mp.pi)
    # Denominator: k! * 2*(2k+3) * gamma(k + 5/2)
    denominator = factorial_k * 2 * (2*k + 3) * gamma_term
    # Current term in the series
    term = numerator / denominator
    # Add term to the result
    result += term
    # Check if term is smaller than 1e-15 to break the loop
    if mp.fabs(term) < 1e-15:
        break
    k += 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))