import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the first term: -π³/36
term1 = - (mp.pi ** 3) / 36

# Compute the Clausen function values for specific arguments
c1 = mp.clsin(2, mp.pi / 3)      # Cl₂(π/3)
c2 = mp.clsin(2, 2 * mp.pi / 3)  # Cl₂(2π/3)

# Compute the second term: -ln(2) * Cl₂(π/3)
term2 = - mp.log(2) * c1

# Initialize sums for the two parts of the series
s1 = mp.mpf(0)  # Sum for coefficients of c1
s2 = mp.mpf(0)  # Sum for coefficients of c2

tolerance = mp.mpf(1e-15)  # Tolerance for stopping the summation
max_m = 1000000            # Maximum number of iterations to prevent infinite loops
m = 0

# Sum over m until terms are below tolerance or max_m is reached
while m <= max_m:
    # Convert indices to mpmath floats for high precision
    a1 = mp.mpf(6 * m + 1)
    a5 = mp.mpf(6 * m + 5)
    a2 = mp.mpf(6 * m + 2)
    a4 = mp.mpf(6 * m + 4)
    
    # Compute the terms for the current m
    term_s1 = 1 / (a1 ** 2) - 1 / (a5 ** 2)  # Coefficient for c1
    term_s2 = 1 / (a2 ** 2) - 1 / (a4 ** 2)  # Coefficient for c2
    
    # Check if both terms are below the tolerance
    if mp.fabs(term_s1) < tolerance and mp.fabs(term_s2) < tolerance:
        break
    
    s1 += term_s1
    s2 += term_s2
    m += 1

# Combine the series sums with Clausen values
series_sum = c1 * s1 + c2 * s2

# Compute the third term: -2 * (c1*s1 + c2*s2)
term3 = -2 * series_sum

# Sum all terms for the final result
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))