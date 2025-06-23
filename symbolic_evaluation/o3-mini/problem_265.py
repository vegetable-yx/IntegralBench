import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value - can be changed as needed)
a_val = 1.0

# Calculate Bessel function terms
J0 = mp.besselj(0, a_val)  # J0(a)
J1 = mp.besselj(1, a_val)  # J1(a)
J2 = mp.besselj(2, a_val)  # J2(a)

# Compute components of the numerator
term1 = 2 * J0
term2 = (a_val**2 - 2) * J1
term3 = -a_val * J2

# Combine terms to get numerator
numerator = term1 + term2 + term3

# Compute denominator
denominator = 8 * a_val

# Final result
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))