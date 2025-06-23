import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate modified Bessel functions of the first kind
I_3_2 = mp.besseli(1.5, 5)  # I_{3/2}(5)
I_5_2 = mp.besseli(2.5, 5)  # I_{5/2}(5)

# Compute terms with coefficients
term1 = 25 * I_3_2
term2 = 3 * I_5_2

# Sum the Bessel function terms
sum_terms = term1 + term2

# Calculate the constant coefficient
coefficient = mp.mpf(125) / 8

# Combine all components for final result
result = coefficient * sqrt_pi * sum_terms

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))